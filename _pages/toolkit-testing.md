---
layout: page
permalink: /toolkit-testing/
title: Toolkit Testing
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
      <li>Literacy domains and subdomains, which you can learn more about on the <a href="../literacy-domains/">literacy domains overview page</a></li>
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
    {% for resource in site.data.cards.resources %}
    <li><b><i class="{{ resource.icon }}"></i> {{ resource.name }}:</b> 
      {% case resource.name %}
      {% when 'Term' %}
      Concepts that are key to each subdomain along with brief definitions and identification of source. Most of the concepts are discussed in the subdomain's open-access readings.
      {% when 'Reading' %}
      Open-access sources that introduce students to important frameworks, concepts, practices, and strategies for doing data advocacy. A list of closed access content is also included on some occasions.
      {% when 'Assignment' %}
      Formal work that gives students opportunity to learn, practice, and reflect on their experiences with data advocacy. These assignments can also be used to assess student learning in relation to each data literacy domain and subdomain.
      {% when 'Activity' %}
      Open-access lessons developed by the Data Advocacy for All team, varying in length and scope, that can be implemented in the classroom to help students hone their abilities to work with data in several literacy domains and subdomains.
      {% when 'Tutorial' %}
      Step-by-step instructions for using various open-access digital tools to work with data. All tutorials rely on minimal computing, so no previous computer experience is required.
      {% when 'Lesson Plan' %}
      A structured collection of resources to help students gain experience with a particular subdomain. This may include readings, glossary, activities, tutorials, etc.
      {% when 'Example Project' %}
      A collection of projects and advocacy movements that utilize data advocacy to bring about social change. Some of these examples are referenced in activities, assignments, modules, and tutorials, while others are simply listed to further model for data advocacy.
      {% when 'Slides' %}
      Open-access slide decks curated by Data Advocacy for All team members to assist the teaching of data advocacy and help hone students hone the multiple literacies needed to do data advocacy is ethical, responsible, and persuasive ways. Many slide decks correspond with specific activities and assignments listed under the various literacy subdomains.
      {% endcase %}
    </li>
    <br>
    {% endfor %}
  </ul>
  </div>
</details>

<br>

## Explore the Toolkit

<!-- Resource Type Button System -->
<div id="resource-type-buttons" class="mb-4">
  <h5>Filter by Resource Type:</h5>
  <div class="button-grid">
    <button class="btn btn-outline-primary active" data-resource="all">
      <i class="fas fa-globe"></i> All Resources
    </button>
    {% for resource in site.data.cards.resources %}
    <button class="btn btn-outline-primary" data-resource="{{ resource.name }}">
      <i class="{{ resource.icon }}"></i> {{ resource.name }}
    </button>
    {% endfor %}
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const resourceButtons = document.querySelectorAll('#resource-type-buttons .btn');
  resourceButtons.forEach(button => {
    button.addEventListener('click', function() {
      resourceButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      filterCards();
    });
  });

  function filterCards() {
    const selectedResource = document.querySelector('#resource-type-buttons .btn.active').dataset.resource;
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
      const cardResource = card.querySelector('.resource').textContent.trim().replace('Type of Resource: ', '');
      if (selectedResource === 'all' || cardResource === selectedResource) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
});
</script>

<div id="filter-container">
  <div id="domain-filter">
    <h5>Filter by Domain:</h5>
    <div class="domain-buttons">
      <button class="btn btn-lg btn-outline-primary domain-btn active" data-domain="all">
        <i class="fas fa-globe"></i> All Domains
      </button>
      <button class="btn btn-lg btn-outline-primary domain-btn" data-domain="Understanding Data">
        <i class="fas fa-brain"></i> Understanding Data
      </button>
      <button class="btn btn-lg btn-outline-primary domain-btn" data-domain="Processing Data">
        <i class="fas fa-cogs"></i> Processing Data
      </button>
      <button class="btn btn-lg btn-outline-primary domain-btn" data-domain="Persuading with Data">
        <i class="fas fa-chart-line"></i> Persuading with Data
      </button>
    </div>
  </div>
</div>

<div id="subdomain-filter" class="mt-4">
  <h5>Filter by Subdomain:</h5>
  <div id="subdomain-buttons">
    <!-- Subdomain buttons will be dynamically populated here -->
  </div>
</div>
<br>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const domainButtons = document.querySelectorAll('.domain-btn');
  const subdomainButtonsContainer = document.getElementById('subdomain-buttons');
  const resourceButtons = document.querySelectorAll('#resource-type-buttons .btn');
  const cards = document.querySelectorAll('.card');

  const subdomains = {
    "Understanding Data": ["Defining Data", "Critiquing Data", "Acting Ethically with Data", "Advocating with Data"],
    "Processing Data": ["Collecting Data", "Preparing Data", "Analyzing Data", "Storing and Preserving Data"],
    "Persuading with Data": ["Making Claims with Data", "Visualizing Data", "Mapping Data", "Telling Stories with Data"]
  };

  let currentDomain = 'all';
  let currentSubdomain = null;
  let currentResourceType = 'all';

  function getAllSubdomains() {
    return Object.values(subdomains).flat();
  }

  function updateSubdomainButtons(domain) {
    subdomainButtonsContainer.innerHTML = '';
    let subdomainsToShow = domain === 'all' ? getAllSubdomains() : subdomains[domain];
    
    subdomainsToShow.forEach(subdomain => {
      const button = document.createElement('button');
      button.className = 'btn btn-sm btn-outline-primary subdomain-btn m-1';
      button.textContent = subdomain;
      button.setAttribute('data-subdomain', subdomain);
      if (subdomain === currentSubdomain) {
        button.classList.add('active');
      }
      subdomainButtonsContainer.appendChild(button);
    });

    // Add event listeners to new subdomain buttons
    document.querySelectorAll('.subdomain-btn').forEach(button => {
      button.addEventListener('click', handleSubdomainClick);
    });
  }

  function filterCards() {
    cards.forEach(card => {
      const cardDomains = card.getAttribute('data-domain').split(',');
      const cardSubdomains = card.getAttribute('data-subdomain').split(',');
      const cardResource = card.querySelector('.resource').textContent.trim().replace('Type of Resource: ', '');
      
      const domainMatch = currentDomain === 'all' || cardDomains.includes(currentDomain);
      const subdomainMatch = !currentSubdomain || cardSubdomains.includes(currentSubdomain);
      const resourceMatch = currentResourceType === 'all' || cardResource === currentResourceType;

      if (domainMatch && subdomainMatch && resourceMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  function handleDomainClick() {
    currentDomain = this.getAttribute('data-domain');
    currentSubdomain = null;
    
    domainButtons.forEach(btn => btn.classList.remove('active'));
    this.classList.add('active');

    updateSubdomainButtons(currentDomain);
    filterCards();
  }

  function handleSubdomainClick() {
    if (this.classList.contains('active')) {
      this.classList.remove('active');
      currentSubdomain = null;
    } else {
      document.querySelectorAll('.subdomain-btn').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      currentSubdomain = this.getAttribute('data-subdomain');
    }

    filterCards();
  }

  function handleResourceTypeClick() {
    currentResourceType = this.getAttribute('data-resource');
    
    resourceButtons.forEach(btn => btn.classList.remove('active'));
    this.classList.add('active');

    filterCards();
  }

  // Add click event listeners to domain buttons
  domainButtons.forEach(button => {
    button.addEventListener('click', handleDomainClick);
  });

  // Add click event listeners to resource type buttons
  resourceButtons.forEach(button => {
    button.addEventListener('click', handleResourceTypeClick);
  });

  // Initialize subdomain buttons
  updateSubdomainButtons('all');
  filterCards();
});
</script>

### Old filter system

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

  <!-- Validation to exclude cards without title or description -->

{% if card.title and card.teaser %}

  <div class="card {% if card.inline == false %}hoverable{% endif %}" style="margin-bottom: 20px;" data-domain="{{ card.domain | default: '' | join: ',' }}" data-subdomain="{{ card.subdomain | default: '' | join: ',' }}">
    <div class="row no-gutters">
      <div class="team">
        <div class="card-body">
          {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
            <h5 class="card-title"><i class="{{ resource.icon | default: 'fas fa-file' }}"></i>&nbsp;&nbsp; {{ card.title }}</h5></a>
          <p class="card-text"><small class="test-muted">
            {% if card.metadata.date %}
              <i class="fa-solid fa-calendar"></i>&nbsp; Date: {{ card.metadata.date | custom_date_format }}
            {% endif %}
            {% if card.metadata.date and card.metadata.author %}
              &nbsp;&nbsp;//&nbsp;&nbsp;
            {% endif %}
            {% if card.metadata.author %}
              <i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.metadata.author | replace: '<br />', ', ' }}
            {% endif %}
          </small></p>
          {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
            <p class="card-text">
              {% assign words = card.teaser | default: '' | number_of_words %}
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
          {% if card.metadata.source or card.metadata.license %}
            <hr class="solid">
          {% endif %}
          <p class="card-text">
            {% if card.metadata.source %}
              <small class="test-muted"><i class="fas fa-link"></i> Source: <a href="{{ card.metadata.source }}">{{ card.metadata.source | replace: '<br />', ', ' }}</a></small>
            {% endif %}
            {% if card.metadata.source and card.metadata.license %}
              <br>
            {% endif %}
            {% if card.metadata.license %}
              <small class="test-muted"><i class="fa-solid fa-quote-left"></i>&nbsp; License: {{ card.metadata.license }}</small>
            {% endif %}
          </p>
          <hr class="solid">
          <p class="card-text">
            <!-- rendering multiple domains vs. single domain -->
            {% assign domain_array = card.domain %}
            <small class="test-muted domain"><i class="fa-solid fa-network-wired"></i>&nbsp; Domain:
              {% for d in domain_array %}
                {% unless forloop.last %}
                  <a href="{{ site.url }}{{ site.baseurl }}/{{ d | downcase | replace: ' ', '-' }}">{{ d }}</a>,&nbsp;
                {% else %}
                  <a href="{{ site.url }}{{ site.baseurl }}/{{ d | downcase | replace: ' ', '-' }}">{{ d }}</a>&nbsp;&nbsp;//&nbsp;&nbsp;
                {% endunless %}
              {% endfor %}
            </small>
            <!-- rendering multiple subdomains vs. single subdomain -->
            {% assign subdomain_array = card.subdomain %}
            <small class="test-muted subdomain"><i class="fa-solid fa-sitemap"></i>&nbsp; Subdomain:
              {% for sub in subdomain_array %}
                {% unless forloop.last %}
                  {{ sub }},&nbsp;
                {% else %}
                  {{ sub }}&nbsp;&nbsp;//&nbsp;&nbsp;
                {% endunless %}
              {% endfor %}
            </small>
            <small class="test-muted resource"><i class="{{ resource.icon | default: 'fas fa-file' }}"></i>&nbsp; Type of Resource: {{ card.resource }}</small><br>
          </p>
        </div>
      </div>
    </div>
  </div>
  {% endif %}
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const domainFilter = document.getElementById('domain-filter');
  const subdomainFilter = document.getElementById('subdomain-filter');
  const resourceFilter = document.getElementById('resource-filter');
  const searchInput = document.getElementById('search-input');
  const clearSearchBtn = document.getElementById('clear-search');
  const searchBtn = document.getElementById('search-button');
  const cards = document.querySelectorAll('.card');

  const subdomainToDomain = {
    'All': 'All',
    'Defining Data': 'Understanding Data',
    'Critiquing Data': 'Understanding Data',
    'Acting Ethically with Data': 'Understanding Data',
    'Advocating with Data': 'Understanding Data',
    'Collecting Data': 'Processing Data',
    'Preparing Data': 'Processing Data',
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
    const searchKeyword = searchInput.value.toLowerCase();

    cards.forEach(card => {
      const cardDomains = card.getAttribute('data-domain').split(',');
      const cardSubdomains = card.getAttribute('data-subdomain').split(',');
      const cardResource = card.querySelector('.resource').textContent.trim().replace('Type of Resource: ', '');
      const cardText = card.textContent.toLowerCase();

      const domainMatch = selectedDomain === 'all' || cardDomains.includes(selectedDomain);
      const subdomainMatch = selectedSubdomain === 'all' || cardSubdomains.includes(selectedSubdomain);
      const resourceMatch = selectedResource === 'all' || cardResource === selectedResource;
      const searchMatch = searchKeyword === '' || cardText.includes(searchKeyword);

      if (domainMatch && subdomainMatch && resourceMatch && searchMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  domainFilter.addEventListener('change', function() {
    subdomainFilter.value = 'all';
    filterCards();
  });

  subdomainFilter.addEventListener('change', function() {
    const selectedSubdomain = subdomainFilter.value;
    const correspondingDomain = subdomainToDomain[selectedSubdomain];
    if (correspondingDomain) {
      domainFilter.value = correspondingDomain;
    } else if (selectedSubdomain === 'all') {
      domainFilter.value = 'all';
    }
    filterCards();
  });
  
  resourceFilter.addEventListener('change', filterCards);
  searchInput.addEventListener('input', filterCards);
  clearSearchBtn.addEventListener('click', function() {
    domainFilter.value = 'all';
    subdomainFilter.value = 'all';
    resourceFilter.value = 'all';
    searchInput.value = '';
    filterCards();
  });

  window.addEventListener('pageshow', initialize);
  initialize();
});
</script>
