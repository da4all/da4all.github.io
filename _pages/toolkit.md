---
layout: page
permalink: /toolkit/
title: Toolkit
description: 
nav: true
nav_rank: 5
---

## Overview

With the Data Advocacy for All toolkit, you can either [explore by the resources organized by literacy domain](../literacydomains/)—or by the type of resource. 

### Resource Types
- **Terms:** Terms refer to concepts that are key to each subdomain along with brief definitions and identification of source. Most of the concepts are discussed in the subdomain’s open access readings.
- **Readings:** Readings include open access sources that introduce students to important frameworks, concepts, practices, and strategies for doing data advocacy. A list of closed access content is also included on some occasions.
- **Assignments:** Assignments include formal work that gives students opportunity to learn, practice, and reflect on their experiences with data advocacy. These assignments can also be used to assess student learning in relation to each data literacy domain and subdomain. 
- **Activities:** Activities include open-access lessons, varying in length and scope, that can be implemented in the classroom to help students hone their abilities to work with data in several literacy domains and subdomains.
- **Tutorials:** Tutorials include step-by-step instructions for using various open-access digital tools to work with data. All tutorials rely on minimal computing, so no previous computer experience is required.
- **Teaching Modules:** Teaching Modules include lesson plans that can be taught in sequence to help students gain experience with a particular literacy domain or subdomain. While all modules include readings, glossary, activities, and formal assignments, some modules also include tutorials.
- **Datasets:** Datasets are freely accessible collections of information that can be used for inquiry, learning, and/or practice. Some datasets are referenced in activities, assignments, modules, and tutorials, while others are simply listed as potential resources and/or models for data advocacy. 
- **Examples of Data Advocacy:** Examples of Data Advocacy are a collection of projects and advocacy movements that utilize data advocacy to bring about social change. Like the datasets, some of these examples are referenced in activities, assignments, modules, and tutorials, while others are simply listed to further model for data advocacy.


## Explore the Resources

<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    
    <label for="resource-filter">Type of Resource:</label>
    <select id="resource-filter">
      <option value="all">All</option>
      {% for resource in site.data.cards.resources %}
      <option value="{{ resource }}">{{ resource }}</option>
      {% endfor %}
    </select>

    <br>
    
    <label for="domain-filter">Primary Domain:</label>
    <select id="domain-filter">
      <option value="all">All</option>
      {% for domain in site.data.cards.domains %}
      <option value="{{ domain }}">{{ domain }}</option>
      {% endfor %}
    </select>

    <br>

    <label for="subdomain-filter">Subdomain:</label>
    <select id="subdomain-filter">
      <option value="all">All</option>
      {% for subdomain in site.data.cards.subdomains %}
      <option value="{{ subdomain }}">{{ subdomain }}</option>
      {% endfor %}
    </select>
    
  </div>
</div>

<div id="card-list" style="margin-top: 20px;">
  {% assign cards = site.cards | sort: "title" %}
  {% for card in cards %}
    <div class="card {% if card.inline == false %}hoverable{% endif %}" style="margin-bottom: 20px;" data-domain="{{ card.domain }}" data-subdomain="{{ card.subdomain }}">
      <div class="row no-gutters">
        <div class="team">
          <div class="card-body">
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <h5 class="card-title">{{ card.title }}</h5></a>
            <p class="card-text"><small class="test-muted">{% if card.profile.date %}<i class="fa-solid fa-calendar"></i>&nbsp; Date: {{ card.profile.date | replace: '<br />', ', ' }}{% endif %}
              {% if card.profile.date and card.profile.author %}&nbsp;&nbsp;//&nbsp;&nbsp;{% endif %}
              {% if card.profile.author %}<i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.profile.author | replace: '<br />', ', ' }}{% endif %}</small></p>
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <p class="card-text">{{ card.teaser }}</p></a>
            {% if card.profile.source or card.profile.license %}
              <hr class="solid">
            {% endif %}
            <p class="card-text">
              {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i> Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a></small>{% endif %}
              {% if card.profile.source and card.profile.license %}<br>{% endif %}
              {% if card.profile.license %}<small class="test-muted"><i class="fa-solid fa-quote-left"></i>&nbsp; License: {{ card.profile.license }}</small>{% endif %}
            </p>
              <hr class="solid">
            <p class="card-text">
              <small class="test-muted domain"><i class="fa-solid fa-square"></i>&nbsp; Domain: <a href="{{ site.url }}{{ site.baseurl }}{{ card.domain | downcase | replace: ' ', '-' }}">{{ card.domain }}</a> &nbsp;&nbsp;//&nbsp;&nbsp;</small>
              <small class="test-muted subdomain"><i class="fa-solid fa-sitemap"></i>&nbsp; Subdomain: {{ card.subdomain }} &nbsp;&nbsp;//&nbsp;&nbsp;</small>
              <small class="test-muted resource"><i class="fa-solid fa-file"></i>&nbsp; Type of Resource: {{ card.resource }}</small><br>
            </p>
          </div>
        </div>
      </div>
    </div>
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const domainFilter = document.getElementById('domain-filter');
  const subdomainFilter = document.getElementById('subdomain-filter');
  const resourceFilter = document.getElementById('resource-filter');
  const cards = document.querySelectorAll('.card');

  function filterCards() {
    const selectedDomain = domainFilter.value;
    const selectedSubdomain = subdomainFilter.value;
    const selectedResource = resourceFilter.value;

    cards.forEach(card => {
      const domain = card.getAttribute('data-domain'); // Get domain from data attribute
      const subdomain = card.getAttribute('data-subdomain'); // Get subdomain from data attribute
      const resource = card.querySelector('.resource').textContent.trim().replace('Type of Resource: ', ''); 

      const domainMatch = selectedDomain === 'all' || domain === selectedDomain;
      const subdomainMatch = selectedSubdomain === 'all' || subdomain === selectedSubdomain;
      const resourceMatch = selectedResource === 'all' || resource === selectedResource;

      if (domainMatch && subdomainMatch && resourceMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  domainFilter.addEventListener('change', filterCards);
  subdomainFilter.addEventListener('change', filterCards);
  resourceFilter.addEventListener('change', filterCards);

  // Initial filtering when the page loads
  filterCards();
});
</script>
