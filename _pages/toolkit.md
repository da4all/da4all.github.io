---
layout: page
permalink: /toolkit/
title: Toolkit
description: 
nav: true
nav_order: 5
---

## Overview

With the Data Advocacy for All toolkit, you can either [explore by the resources organized by literacy domain](../literacy-domains/)—or by the type of resource.

<details>
  <summary>Instructions for Using the Toolkit</summary>
  <div class="content">
    This toolkit works on a filtering reduction model, meaning that all cards initially populate and then are reduced to fit any filtering criteria submitted. 
    <br><br>
    You can filter the toolkit below by:
    <ul>
      <li>Type of resource, with a full list below specifying the various resource types</li>
      <li>Literacy domains and subdomains, which you can learn more about on the <a href="../literacydomains/">literacy domains overview page</a></li>
      <li>A custom search, which will populate as you type or whenever you click the "search" button; the "clear search" button will clear all search results</li>
    </ul>
  </div>
</details>

<div style="height:5px;font-size:1px;">&nbsp;<br></div>
<div style="height:5px;font-size:1px;">&nbsp;</div>

<details>
  <summary>Resource Types</summary>
  <div class="content">
  <ul>
    <li><b>Terms:</b> Terms refer to concepts that are key to each subdomain along with brief definitions and identification of source. Most of the concepts are discussed in the subdomain’s open access readings.</li>
    <br>
    <li><b>Readings:</b> Readings include open access sources that introduce students to important frameworks, concepts, practices, and strategies for doing data advocacy. A list of closed access content is also included on some occasions.</li>
    <br>
    <li><b>Assignments:</b> Assignments include formal work that gives students opportunity to learn, practice, and reflect on their experiences with data advocacy. These assignments can also be used to assess student learning in relation to each data literacy domain and subdomain. </li>
    <br>
    <li><b>Activities:</b> Activities include open-access lessons, varying in length and scope, that can be implemented in the classroom to help students hone their abilities to work with data in several literacy domains and subdomains.</li>
    <br>
    <li><b>Tutorials:</b> Tutorials include step-by-step instructions for using various open-access digital tools to work with data. All tutorials rely on minimal computing, so no previous computer experience is required.</li>
    <br>
    <li><b>Teaching Modules:</b> Teaching Modules include lesson plans that can be taught in sequence to help students gain experience with a particular literacy domain or subdomain. While all modules include readings, glossary, activities, and formal assignments, some modules also include tutorials.</li>
    <br>
    <li><b>Datasets:</b> Datasets are freely accessible collections of information that can be used for inquiry, learning, and/or practice. Some datasets are referenced in activities, assignments, modules, and tutorials, while others are simply listed as potential resources and/or models for data advocacy. </li>
    <br>
    <li><b>Examples of Data Advocacy:</b> Examples of Data Advocacy are a collection of projects and advocacy movements that utilize data advocacy to bring about social change. Like the datasets, some of these examples are referenced in activities, assignments, modules, and tutorials, while others are simply listed to further model for data advocacy.</li></ul></div>
</details>

<br>

## Explore the Toolkit

<div style="background-color: #f2f2f2; padding: 10px;">
  <div id="filter-options" style="font-size: 0.8em;">
    
    <label for="resource-filter">Type of Resource:</label>
    <select id="resource-filter">
      <option value="all">All</option>
      {% for resource in site.data.cards.resources %}
      <option value="{{ resource.name }}">{{ resource.name }}</option>
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
    
    <br>
    
    <label for="search-input">Search:</label>
    <input type="text" id="search-input" style="width: 300px;" placeholder="Search by word, phrase, or keyword">
    <button id="search-button">Search</button>
    <button id="clear-search">Clear Search</button>

  </div>
</div>

{% assign cards = site.cards | sort: "title" %}

<div id="card-list" style="margin-top: 20px;">
  {% for card in cards %}
  {% assign resource = site.data.cards.resources | where: "name", card.resource | first %}
  <div class="card {% if card.inline == false %}hoverable{% endif %}" style="margin-bottom: 20px;" data-domain="{{ card.domain }}" data-subdomain="{{ card.subdomain }}">
    <div class="row no-gutters">
      <div class="team">
        <div class="card-body">
          {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
            <h5 class="card-title"><i class="{{ resource.icon | default: 'fas fa-file' }}"></i>&nbsp;&nbsp; {{ card.title }}</h5></a>
          <p class="card-text"><small class="test-muted">{% if card.profile.date %}<i class="fa-solid fa-calendar"></i>&nbsp; Date: {{ card.profile.date | replace: '<br />', ', ' }}{% endif %}
            {% if card.profile.date and card.profile.author %}&nbsp;&nbsp;//&nbsp;&nbsp;{% endif %}
            {% if card.profile.author %}<i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.profile.author | replace: '<br />', ', ' }}{% endif %}</small></p>
          {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
            <p class="card-text">
              {% assign words = card.teaser | number_of_words %}
              {% if words > 150 %}
              {% assign teaser_words = card.teaser | split: ' ' | slice: 0, 150 | join: ' ' %}
              {{ teaser_words }} <span style="color: #0140A8;">[Read More]</span>
              {% else %}
              {{ card.teaser }}
              {% endif %}
            </p>
          {% if card.keywords.size > 0 %}
            <hr class="solid">
            <p class="card-text test-muted keyword"><small>Keywords: {% for keyword in card.keywords %}<i class="fa-solid fa-hashtag fa-sm"></i>&nbsp;{{ keyword }}&nbsp;&nbsp;{% endfor %}</small></p>
            {% endif %}
            </a>
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
                <small class="test-muted resource"><i class="{{ resource.icon | default: 'fas fa-file' }}"></i>&nbsp; Type of Resource: {{ card.resource }}</small><br>
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
  const keywordLinks = document.querySelectorAll('.keyword-filter');
  const cards = document.querySelectorAll('.card');
  const searchInput = document.getElementById('search-input');
  const clearSearchBtn = document.getElementById('clear-search');
  const searchBtn = document.getElementById('search-button');

  // Define a mapping of subdomains to corresponding domains
  const subdomainToDomain = {
    'All': 'All',
    'Defining Data': 'Understanding Data',
    'Critiquing Data': 'Understanding Data',
    'Acting Ethically with Data': 'Understanding Data',
    'Advocating with Data': 'Understanding Data',
    'Collecting Data': 'Processing Data',
    'Organizing and Cleaning Data': 'Processing Data',
    'Analyzing Data': 'Processing Data',
    'Storing and Preserving Data': 'Processing Data',
    'Making Claims with Data': 'Persuading with Data',
    'Visualizing Data': 'Persuading with Data',
    'Mapping Data': 'Persuading with Data',
    'Telling Stories with Data': 'Persuading with Data'
  };

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

  domainFilter.addEventListener('change', function() {
    // Reset the subdomain filter to "All" when the domain filter changes
    subdomainFilter.value = 'all';
    filterCards();
  });

  subdomainFilter.addEventListener('change', function() {
    // Update the domain filter based on the selected subdomain
    const selectedSubdomain = subdomainFilter.value;
    const correspondingDomain = subdomainToDomain[selectedSubdomain];
    if (correspondingDomain) {
      domainFilter.value = correspondingDomain;
    } else if (selectedSubdomain === 'all') {
      domainFilter.value = 'all'; // Set domain filter to 'all' if 'all' is selected for subdomain
    }
    filterCards();
  });
  
  resourceFilter.addEventListener('change', filterCards);

  keywordLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      const selectedKeyword = this.getAttribute('data-keyword');
      filterCardsByKeyword(selectedKeyword);
    });
  });

  searchInput.addEventListener('input', function() {
    filterCardsBySearch(this.value.trim());
  });

  searchBtn.addEventListener('click', function() {
    searchInput.form.submit();
  });

  clearSearchBtn.addEventListener('click', function() {
    searchInput.value = '';
    filterCardsBySearch('');
  });

  function filterCardsBySearch(keyword) {
    cards.forEach(card => {
      const cardText = card.textContent.toLowerCase();
      if (cardText.includes(keyword.toLowerCase())) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // Set the filters to default values on page load
  function resetFilters() {
    domainFilter.value = 'all';
    subdomainFilter.value = 'all';
    resourceFilter.value = 'all';
    searchInput.value = '';
  }

  // Initial filtering when the page loads
  function initialize() {
    resetFilters();
    filterCards();
  }

  // Handle both DOMContentLoaded and pageshow events
  window.addEventListener('pageshow', initialize);
  initialize();
});
</script>
