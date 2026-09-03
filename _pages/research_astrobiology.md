---
layout: page
title: Astrobiology
permalink: /research/astrobiology/
description: Research articles on planetary habitability, atmospheric evolution, and astrobiology.
nav: false
topic: astrobiology
---

<link rel="stylesheet" href="{{ '/assets/css/research.css' | relative_url }}">

<a class="research-back-link" href="{{ '/research/' | relative_url }}"><span aria-hidden="true">←</span> All research themes</a>

<div class="research-topic-hero">
  <img
    src="{{ '/assets/img/research/astrobiology.webp' | relative_url }}"
    alt="A potentially habitable ocean world viewed from space"
    loading="eager"
  >
</div>

<p class="research-topic-intro">
  Astrobiology connects planetary environments, the energetics of life, and the search for biological and technological signatures. My work
  asks how physically measurable quantities can place life and technology in a common comparative framework, from Solar System worlds to
  exoplanets that future observatories may characterize.
</p>

<h2 class="research-archive-heading">Research highlights</h2>

<div class="research-feature-list">
  <article class="research-feature research-feature--article">
    <div class="research-feature__copy">
      <time datetime="2026-09">September 2026 · Under review in <i>Astrobiology</i></time>
      <h3>
        <a href="https://arxiv.org/search/?query=Energetic+Decoupling+from+Biological+Scaling&amp;searchtype=title">
          Energetic Decoupling from Biological Scaling: A Dimensionless Framework for Technological Civilizations
        </a>
      </h3>
      <p>
        This novel study extends species-level biological scaling by treating externally harvested technological energy as a separate part of
        a civilization's power budget. It introduces two dimensionless coordinates: the biological decoupling parameter,
        <i>ν</i> = P<sub>ext</sub>/P<sub>bio</sub>, and the environmental utilization parameter,
        <i>κ</i> = P<sub>ext</sub>/P<sub>available</sub>. The first measures how far technological power has moved beyond collective metabolism;
        the second measures how much of an explicitly defined environmental energy resource is being used.
      </p>
      <p>
        Together, <i>ν</i> and <i>κ</i> define a continuous phase space connecting biological organisms, present-day technological societies,
        and Kardashev-type civilizations without relying only on absolute power consumption. In the adopted planetary-energy normalization,
        modern humanity has <i>ν</i> ≈ 24 but <i>κ</i> ≈ 1.1 × 10<sup>-4</sup>: technological power already exceeds collective metabolism,
        while only a small fraction of the accessible planetary energy resource is used.
      </p>
      <p>
        The framework also provides a common language for interpreting technosignatures. Reflected-light spectra illustrate how industrial
        gases such as CF<sub>4</sub> and SF<sub>6</sub> could alter an Earth-like planet's spectrum, connecting future atmospheric measurements
        to model-dependent bounds on a civilization's energetic state.
      </p>
      <div class="research-link-row">
        <a href="https://arxiv.org/search/?query=Energetic+Decoupling+from+Biological+Scaling&amp;searchtype=title">arXiv record</a>
      </div>
      <p class="research-link-note">The title link points to an arXiv title search and can be replaced with the final abstract URL once posted.</p>
    </div>
  </article>
</div>

<div class="research-figure-grid research-figure-grid--stacked">
  <figure>
    <img
      src="{{ '/assets/img/research/astrobiology-energetic-phase-space.png' | relative_url }}"
      alt="Energetic phase space defined by biological decoupling and environmental utilization, showing planetary, stellar, and galactic domains"
      loading="lazy"
    >
    <figcaption>
      <strong>Figure 1.</strong> The energetic phase space. Civilizations move along domain-dependent trajectories as technological power grows;
      transitions to stellar and galactic domains connect naturally to Kardashev Types II and III.
    </figcaption>
  </figure>
  <figure>
    <img
      src="{{ '/assets/img/research/astrobiology-reflected-light-spectra.png' | relative_url }}"
      alt="Model reflected-light spectra for pre-agricultural Earth, modern Earth, and advanced technological atmospheric scenarios"
      loading="lazy"
    >
    <figcaption>
      <strong>Figure 2.</strong> Example reflected-light spectra for pre-agricultural Earth, modern Earth, and technological scenarios. The most
      industrialized example includes enhanced CO<sub>2</sub> drawdown and 10 ppm CF<sub>4</sub> and SF<sub>6</sub>.
    </figcaption>
  </figure>
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
