---
layout: page
permalink: /publications/
title: publications
description: Publications on exoplanet atmospheres, planetary systems, astrobiology, and instrumentation.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->

Publications are organized by review and authorship status, with the most recent work first in each section. Links to the DOI, arXiv record, or publisher page appear below each citation. For a continuously updated record, see
[NASA ADS](https://ui.adsabs.harvard.edu/search/q=author%3A%22Krishnamurthy%2C%20Vigneshwaran%22&sort=date%20desc%2C%20bibcode%20desc&p_=0) or
[Google Scholar](https://scholar.google.com/citations?user=7xSicYwAAAAJ).

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

## Under review

{% bibliography --query @*[section=under_review] %}

## First- and second-author publications

{% bibliography --query @*[section=primary] %}

## Research briefings

{% bibliography --query @*[section=briefing] %}

## Nth-author publications

{% bibliography --query @*[section=coauthored] %}

</div>
