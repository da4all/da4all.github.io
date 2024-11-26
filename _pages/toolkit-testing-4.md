---
layout: page
permalink: /toolkit-testing-4/
title: Toolkit Testing Option 4
description:
nav: false
nav_order: 5
---

Welcome to the Data Advocacy for All Toolkit! This is a curated collection of teaching resources designed to support data advocacy, including readings, assignments, lesson plans, and more. Our lessons are organized by both what [type of resource](../resource-types/) they are and what data advocacy [literacy domain](../literacy-domains/) they fall under. Use the buttons below to filter resources by their `Resource Type` and `Literacy Domain/Subdomain`, or search for specific topics or keywords across the resources.

<!-- Resource Type Filter Section -->
<div class="filter-section mb-4">
  <h3>Filter by Resource Type</h3>
  <div class="button-grid resource-grid">
    {% assign resources = site.data.cards.resources %}
    {% for resource in resources %}
    <button class="filter-btn resource-btn" data-filter="resource" data-value="{{ resource.name }}">
      <i class="{{ resource.icon }}"></i>
      {{ resource.name }}
    </button>
    {% endfor %}
  </div>
  <button class="reset-btn" data-reset="resource">
    Show All Resources
  </button>
</div>

<!-- Domain Filter Section -->
<div class="filter-section mb-4">
  <h3>Filter by Domain</h3>
  <div class="button-grid domain-grid">
    {% for domain in site.data.cards.domains %}
    <button class="filter-btn domain-btn" data-filter="domain" data-value="{{ domain }}">
      <i class="{% case domain %}
        {% when 'Understanding Data' %}fas fa-brain
        {% when 'Processing Data' %}fas fa-cogs
        {% when 'Persuading with Data' %}fas fa-chart-line
      {% endcase %}"></i>
      {{ domain }}
    </button>
    {% endfor %}
  </div>
  <button class="reset-btn" data-reset="domain">
    Show All Domains
  </button>
</div>

<!-- Subdomain Filter Section (Hidden by default) -->
<div id="subdomain-section" class="filter-section mb-4" style="display: none;">
  <div style="text-align: center;">
    <h4>Filter by Subdomain</h4>
    <div class="button-grid subdomain-grid">
      <!-- Populated dynamically by JavaScript -->
    </div>
  </div>
</div>

<!-- Search Section -->
<div class="search-section mb-4">
  <!--<h3>Search Resources</h3>-->
  <div class="search-container">
    <input type="text" id="search-input" placeholder="Search resources...">
    <button id="search-btn" class="search-btn">Search</button>
    <button id="clear-search-btn" class="search-btn">Clear Search</button>
  </div>
</div>

<!-- Card List Section -->
<h2>Filtered Resources:</h2>
<div id="card-list" style="margin-top: 20px;">
  {% assign cards = site.cards | sort: "title" %}
  {% for card in cards %}
    {% if card.title and card.teaser %}
      <div class="card {% if card.inline == false %}hoverable{% endif %}" 
           data-resource="{{ card.resource }}"
           data-domain="{{ card.domain | join: ',' }}"
           data-subdomain="{{ card.subdomain | join: ',' }}" style="margin-top: 10px;">
        {% assign resource = site.data.cards.resources | where: "name", card.resource | first %}
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
class ToolkitFilter {
  constructor() {
    this.state = {
      resource: null,
      domain: null,
      subdomain: null,
      searchQuery: ''
    };
    
    this.subdomains = {
      'Understanding Data': ['Defining Data', 'Critiquing Data', 'Acting Ethically with Data', 'Thinking Rhetorically about Data'],
      'Processing Data': ['Collecting Data', 'Preparing Data', 'Analyzing Data', 'Storing and Preserving Data'],
      'Persuading with Data': ['Making Claims with Data', 'Visualizing Data', 'Mapping Data', 'Telling Stories with Data']
    };
    
    this.init();
  }

  init() {
    this.bindEvents();
    this.filterCards();
  }

  bindEvents() {
    // Resource filter buttons
    document.querySelectorAll('.resource-btn').forEach(btn => {
      btn.addEventListener('click', () => this.handleFilter('resource', btn));
    });

    // Domain filter buttons
    document.querySelectorAll('.domain-btn').forEach(btn => {
      btn.addEventListener('click', () => this.handleFilter('domain', btn));
    });

    // Reset buttons
    document.querySelectorAll('.reset-btn').forEach(btn => {
      btn.addEventListener('click', () => this.handleReset(btn.dataset.reset));
    });

    // Search functionality
    const searchInput = document.getElementById('search-input');
    
    // Real-time search as user types
    searchInput.addEventListener('input', () => this.handleSearch());
    
    // Handle Enter key press
    searchInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        this.handleSearch();
      }
    });
    
    // Button clicks
    document.getElementById('search-btn').addEventListener('click', () => this.handleSearch());
    document.getElementById('clear-search-btn').addEventListener('click', () => this.clearSearch());
  }

  handleFilter(type, button) {
    const value = button.dataset.value;
    
    // Toggle active state
    if (this.state[type] === value) {
      this.state[type] = null;
      button.classList.remove('active');
    } else {
      // Remove active class from other buttons of same type
      document.querySelectorAll(`.${type}-btn`).forEach(btn => {
        btn.classList.remove('active');
      });
      this.state[type] = value;
      button.classList.add('active');
    }

    // Handle subdomain visibility for domain changes
    if (type === 'domain') {
      this.updateSubdomains();
    }

    this.filterCards();
  }

  filterCards() {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
      const resourceType = card.dataset.resource;
      const domains = card.dataset.domain.split(',');
      const subdomains = card.dataset.subdomain.split(',');
      const cardText = card.textContent.toLowerCase();

      const resourceMatch = !this.state.resource || resourceType === this.state.resource;
      const domainMatch = !this.state.domain || domains.includes(this.state.domain);
      const subdomainMatch = !this.state.subdomain || subdomains.includes(this.state.subdomain);
      const searchMatch = !this.state.searchQuery || cardText.includes(this.state.searchQuery);

      card.style.display = 
        resourceMatch && domainMatch && subdomainMatch && searchMatch 
        ? 'block' 
        : 'none';
    });
  }

  updateSubdomains() {
    const subdomainSection = document.getElementById('subdomain-section');
    const subdomainGrid = document.querySelector('.subdomain-grid');
    
    if (!this.state.domain) {
      subdomainSection.style.display = 'none';
      this.state.subdomain = null;
      return;
    }

    // Show subdomain section and populate buttons
    subdomainSection.style.display = 'block';
    subdomainGrid.innerHTML = '';
    
    this.subdomains[this.state.domain].forEach(subdomain => {
      const button = document.createElement('button');
      button.className = 'filter-btn subdomain-btn';
      button.textContent = subdomain;
      button.dataset.value = subdomain;
      button.addEventListener('click', () => this.handleFilter('subdomain', button));
      subdomainGrid.appendChild(button);
    });
  }

  handleSearch() {
    const searchInput = document.getElementById('search-input');
    this.state.searchQuery = searchInput.value.toLowerCase();
    this.filterCards();
  }

  clearSearch() {
    const searchInput = document.getElementById('search-input');
    searchInput.value = '';
    this.state.searchQuery = '';
    this.filterCards();
  }

  handleReset(type) {
    this.state[type] = null;
    document.querySelectorAll(`.${type}-btn`).forEach(btn => {
      btn.classList.remove('active');
    });
    
    if (type === 'domain') {
      document.getElementById('subdomain-section').style.display = 'none';
      this.state.subdomain = null;
    }
    
    this.filterCards();
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  new ToolkitFilter();
});
</script>

## Filter by Resource Type

<!-- code goes here -->

## Filter by Domain

<!-- code goes here -->

### Filter by Subdomain

<!-- code goes here - this only shows if a button is selected in Domain section -->

## Search Within Resources

<!-- code goes here -->

## Filtered Resources:
