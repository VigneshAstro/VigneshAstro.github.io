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

<div class="research-topic-hero">
  <img
    src="{{ '/assets/img/research/future-telescopes.webp' | relative_url }}"
    alt="A future segmented space telescope observing a distant planetary system"
    loading="eager"
  >
</div>

<p class="research-topic-intro">
  The next generation of ground- and space-based observatories will make it possible to probe smaller and cooler worlds. I am interested in
  the spectroscopic capabilities, observing strategies, and instrument concepts needed to turn faint planetary signals into robust atmospheric
  measurements.
</p>

<h2 class="research-archive-heading">Articles &amp; paper notes</h2>

{% assign research_posts = site.posts | where_exp: "post", "post.categories contains page.topic" | sort: "date" | reverse %}
{% if research_posts.size > 0 %}
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
  <div class="research-empty-state">
    <p>Articles and paper notes will appear here, with the newest first.</p>
  </div>
{% endif %}
