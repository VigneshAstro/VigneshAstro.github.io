---
layout: page
permalink: /publications/
title: Publications
description: Publications on exoplanet atmospheres, planetary systems, astrobiology, and instrumentation.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->

Publications are organized by review and authorship status, with the most recent work first in each section. Links to NASA ADS, arXiv, and the DOI or publisher page appear below each citation. For a continuously updated record, see
[NASA ADS](https://ui.adsabs.harvard.edu/search/q=author%3A%22Krishnamurthy%2C%20Vigneshwaran%22&sort=date%20desc%2C%20bibcode%20desc&p_=0) or
[Google Scholar](https://scholar.google.com/citations?user=7xSicYwAAAAJ).

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<h2 style="font-size: 1.65rem; font-weight: 700; margin-top: 2.5rem;">Under review</h2>

{% bibliography --query @*[section=under_review] %}

<h2 style="font-size: 1.65rem; font-weight: 700; margin-top: 2.5rem;">First- and second-author publications</h2>

{% bibliography --query @*[section=primary] %}

<h2 style="font-size: 1.65rem; font-weight: 700; margin-top: 2.5rem;">Research briefings</h2>

{% bibliography --query @*[section=briefing] %}

<h2 style="font-size: 1.65rem; font-weight: 700; margin-top: 2.5rem;">Nth-author publications</h2>

{% bibliography --query @*[section=coauthored] %}

</div>

<script>
  (() => {
    const formatPublications = () => {
      document.querySelectorAll(".publications li").forEach((publication) => {
        const author = publication.querySelector(".author");
        if (author) {
          author.innerHTML = author.innerHTML
            .replace(/,\s*and\s+others/g, ", et al.")
            .replace(/\s+and\s+others/g, " et al.")
            .replace(/,\s*others/g, ", et al.");

          const periodicals = publication.querySelectorAll(".periodical");
          const coauthorNote = periodicals[1]?.textContent.trim();
          if (coauthorNote?.startsWith("(including Vigneshwaran Krishnamurthy)")) {
            author.insertAdjacentText("beforeend", ` ${coauthorNote}`);
            periodicals[1].remove();
          }
        }

        const links = publication.querySelector(".links");
        if (!links) return;

        links.querySelectorAll("a").forEach((link) => {
          if (link.href.includes("ui.adsabs.harvard.edu")) link.textContent = "NASA ADS";
        });

        const linkOrder = { "NASA ADS": 0, arXiv: 1, DOI: 2, HTML: 3 };
        [...links.children]
          .sort((first, second) => (linkOrder[first.textContent.trim()] ?? 10) - (linkOrder[second.textContent.trim()] ?? 10))
          .forEach((link) => links.appendChild(link));
      });
    };

    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", formatPublications);
    else formatPublications();
  })();
</script>
