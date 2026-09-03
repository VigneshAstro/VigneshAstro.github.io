---
layout: page
title: Future Telescopes & Instruments
permalink: /research/future-telescopes-instruments/
description: Research articles on future telescopes, spectrographs, and instruments for exoplanet science.
nav: false
topic: future-telescopes-instruments
---

<link rel="stylesheet" href="{{ '/assets/css/research.css' | relative_url }}">

<a class="research-back-link" href="{{ '/research/' | relative_url }}"><span aria-hidden="true">←</span> All research themes</a>

<figure class="research-topic-hero">
  <img
    src="{{ '/assets/img/research/nasa-exoplanet-missions.jpg' | relative_url }}"
    alt="NASA graphic showing past, present, and future exoplanet missions"
    loading="eager"
  >
  <figcaption class="research-image-credit">Exoplanet missions and observatories. Credit: NASA.</figcaption>
</figure>

<p class="research-topic-intro">
  Future facilities will move atmospheric characterization toward smaller and cooler worlds while measuring much larger and more diverse
  samples. My work examines the observing strategies and instrument capabilities needed to turn faint planetary signals into robust atmospheric
  measurements, from Ariel's population survey to the direct-imaging era of the Habitable Worlds Observatory.
</p>

<h2 class="research-archive-heading">Research highlights</h2>

<div class="research-feature-list">
  <article class="research-feature research-feature--compact">
    <div class="research-feature__copy">
      <time datetime="2026-09">September 2026 · Under review in the RASTI Ariel Special Issue</time>
      <h3><a href="https://arxiv.org/abs/2609.01577">Beyond Five Scale Heights: Ariel Tier-2 requirements for sub-Neptunes</a></h3>
      <p>
        The Ariel Mission Candidate Sample uses a clear hydrogen-helium atmosphere and a five-scale-height signal as a common screening
        reference. We tested how the Tier-2 observing requirements change for 197 known sub-Neptunes when metallicity and clouds are included
        explicitly. Synthetic spectra at 1×, 10×, and 100× solar metallicity - with clear atmospheres and 1-mbar cloud decks - were evaluated
        in Ariel AIRS channels using target-specific noise estimates.
      </p>
      <p>
        Clear solar-composition atmospheres largely follow the mission reference, but high mean molecular weight and clouds can substantially
        increase the observing time. The 1×-solar cloudy case requires nearly an order of magnitude more transits than the simple prediction,
        and most tested scenarios require more visits for a robust spectral detection. The study also identifies Ariel targets with detected
        metastable helium, connecting lower-atmosphere composition and clouds to extended escaping upper atmospheres.
      </p>
      <div class="research-link-row">
        <a href="https://ui.adsabs.harvard.edu/abs/2026arXiv260901577K/abstract">NASA ADS</a>
        <a href="https://arxiv.org/abs/2609.01577">arXiv</a>
      </div>
    </div>
  </article>

  <article class="research-feature research-feature--status">
    <div class="research-feature__copy">
      <time datetime="2026">Ongoing</time>
      <h3>Preparing for the Habitable Worlds Observatory</h3>
      <p>
        Work is also underway for the Habitable Worlds Observatory (HWO). I am exploring how atmospheric evolution, escape, reflected-light
        spectroscopy, and the interpretation of biosignatures and technosignatures can inform target selection and observing strategies for
        nearby potentially habitable worlds.
      </p>
    </div>
  </article>
</div>

{% assign research_posts = site.posts | where_exp: "post", "post.categories contains page.topic" | sort: "date" | reverse %}
{% if research_posts.size > 0 %}

  <h2 class="research-archive-heading research-archive-heading--secondary">More articles &amp; paper notes</h2>
  <div class="research-article-list">
    {% for post in research_posts %}
      <article class="research-article-card">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        {% if post.description %}<p>{{ post.description }}</p>{% endif %}
        <a class="research-article-card__link" href="{{ post.url | relative_url }}">Read article <span aria-hidden="true">→</span></a>
      </article>
    {% endfor %}
  </div>
{% else %}
{% endif %}
