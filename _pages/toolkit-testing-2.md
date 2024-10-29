---
layout: page
permalink: /toolkit-testing-2/
title: Toolkit Testing Option 2
description:
nav: false
nav_order: 5
---

Welcome to the Data Advocacy for All Toolkit! This is a curated collection of teaching resources designed to support data advocacy, including readings, assignments, lesson plans, and more. Our lessons are organized by both what [type of resource](../resource-types/) they are and what data advocacy [literacy domain](../literacy-domains/) they fall under. Use the buttons below to filter resources by their `Resource Type`, `Literacy Domain`, and `Literacy Subdomain`, or search for specific topics or keywords across the resources.

<!-- Resource Type Button System -->
<div id="resource-type-buttons" class="mb-4">
  <h3 style="text-align: center;">Filter by Resource Type:</h3>
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

<!-- Domain Type Button System -->
<div id="domain-buttons" class="mb-4">
  <h3 style="text-align: center;">Filter by Literacy Domain:</h3>
  <div class="button-grid">
    <button class="btn btn-outline-primary domain-btn active" data-domain="all">
      <i class="fas fa-globe"></i> All Domains
    </button>
    <button type="button" class="btn btn-outline-primary domain-btn" data-domain="Understanding Data">
      <i class="fas fa-brain"></i> Understanding Data
    </button>
    <button class="btn btn-outline-primary domain-btn" data-domain="Processing Data">
      <i class="fas fa-cogs"></i> Processing Data
    </button>
    <button class="btn btn-outline-primary domain-btn" data-domain="Persuading with Data">
      <i class="fas fa-chart-line"></i> Persuading with Data
    </button>
  </div>
</div>

<!-- Subdomain Filter Section (Hidden by default) -->
<div id="subdomain-section" class="mt-4" style="display: none;">
  <h4 style="text-align: center;">Filter by Subdomain:</h4>
  <div id="subdomain-buttons" class="button-grid">
    <!-- Subdomain buttons will be populated dynamically -->
  </div>
</div>

<div id="search-container" class="mt-4">
  <h3 style="text-align: center;">Search Within Resources:</h3>
  <div class="input-group mb-3">
    <input type="text" id="search-input" class="form-control" placeholder="Enter search terms...">
    <div class="input-group-append">
      <button class="btn search-btn" type="button" id="search-button">Search</button>
    </div>
    <div class="input-group-append">
      <button class="btn search-btn" type="button" id="clear-search-button">Clear Search</button>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const domainButtons = document.querySelectorAll('.domain-btn');
  const subdomainSection = document.getElementById('subdomain-section');
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

  function updateSubdomainButtons(domain) {
    const subdomainButtonsContainer = document.getElementById('subdomain-buttons');
    subdomainButtonsContainer.innerHTML = ''; // Clear existing buttons
    
    if (domain === 'all') {
      subdomainSection.style.display = 'none';
      return;
    }

    // Show the subdomain section
    subdomainSection.style.display = 'block';
    
    // Create buttons for the selected domain
    const domainSubdomains = subdomains[domain] || [];
    domainSubdomains.forEach(subdomain => {
      const button = document.createElement('button');
      button.className = 'btn btn-outline-primary subdomain-btn';
      button.textContent = subdomain;
      button.setAttribute('data-subdomain', subdomain);
      subdomainButtonsContainer.appendChild(button);

      // Add click event listener
      button.addEventListener('click', function() {
        const wasActive = this.classList.contains('active');
        
        // Remove active class from all subdomain buttons
        document.querySelectorAll('.subdomain-btn').forEach(btn => {
          btn.classList.remove('active');
        });

        if (!wasActive) {
          this.classList.add('active');
          currentSubdomain = this.getAttribute('data-subdomain');
        } else {
          currentSubdomain = null;
        }

        filterCards();
      });
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

  // Add click event listeners to domain buttons
  domainButtons.forEach(button => {
    button.addEventListener('click', function() {
      const newDomain = this.getAttribute('data-domain');
      
      // Update active state of domain buttons
      domainButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      
      // Update current domain and reset subdomain selection
      currentDomain = newDomain;
      currentSubdomain = null;
      
      // Update subdomain buttons
      updateSubdomainButtons(newDomain);
      
      // Filter cards
      filterCards();
    });
  });

  // Add click event listeners to resource type buttons
  resourceButtons.forEach(button => {
    button.addEventListener('click', function() {
      currentResourceType = this.getAttribute('data-resource');
      resourceButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      filterCards();
    });
  });

  // Initialize the page
  updateSubdomainButtons('all');
  filterCards();
});
</script>

---

## Filtered Resources:

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
