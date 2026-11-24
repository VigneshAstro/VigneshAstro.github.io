"""Check profile selection and safe cache updates without contacting Scholar."""

import importlib.util
import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import Mock, patch

import yaml


ROOT = Path(__file__).resolve().parents[1]


class CitationUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.old_cwd = os.getcwd()
        os.chdir(self.tmp.name)
        self.addCleanup(os.chdir, self.old_cwd)
        Path('_data').mkdir()
        Path('_data/socials.yml').write_text(
            'my_google_scholar:\n  url: https://scholar.google.com/citations?user=7xSicYwAAAAJ\n'
        )
        self.scholar = Mock()
        self.scholar.fill.return_value = {
            'publications': [{
                'author_pub_id': '7xSicYwAAAAJ:example',
                'bib': {'title': 'Example', 'pub_year': '2026'},
                'num_citations': 3,
            }]
        }
        spec = importlib.util.spec_from_file_location('citation_updater', ROOT / 'bin/update_scholar_citations.py')
        self.module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {'scholarly': types.SimpleNamespace(scholarly=self.scholar)}):
            spec.loader.exec_module(self.module)

    def test_custom_profile_and_first_refresh(self):
        self.assertEqual(self.module.SCHOLAR_USER_ID, '7xSicYwAAAAJ')
        self.module.get_scholar_citations()
        data = yaml.safe_load(Path('_data/citations.yml').read_text())
        self.assertEqual(data['metadata']['scholar_user_id'], '7xSicYwAAAAJ')
        self.assertEqual(data['papers']['7xSicYwAAAAJ:example']['citations'], 3)

    def test_fetch_failure_preserves_cache(self):
        cache = Path('_data/citations.yml')
        cache.write_text('metadata: {}\npapers: {existing: {citations: 4}}\n')
        before = cache.read_bytes()
        self.scholar.search_author_id.side_effect = RuntimeError('Request blocked')
        with self.assertRaises(SystemExit):
            self.module.get_scholar_citations()
        self.assertEqual(cache.read_bytes(), before)

    def test_empty_result_preserves_cache(self):
        cache = Path('_data/citations.yml')
        cache.write_text('metadata: {}\npapers: {existing: {citations: 4}}\n')
        before = cache.read_bytes()
        self.scholar.fill.return_value = {'publications': []}
        with self.assertRaises(SystemExit):
            self.module.get_scholar_citations()
        self.assertEqual(cache.read_bytes(), before)

    def test_another_profiles_cache_does_not_skip_refresh(self):
        Path('_data/citations.yml').write_text(yaml.safe_dump({
            'metadata': {'last_updated': self.module.datetime.now().strftime('%Y-%m-%d'), 'scholar_user_id': 'template-id'},
            'papers': {},
        }))
        self.module.get_scholar_citations()
        self.scholar.search_author_id.assert_called_once_with('7xSicYwAAAAJ')


if __name__ == '__main__':
    unittest.main()
