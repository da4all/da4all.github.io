---
layout: page
permalink: /toolkit/
title: Toolkit
description:
nav: true
nav_order: 1
---

Welcome to the Data Advocacy for All Toolkit! This is a curated collection of teaching resources designed to support data advocacy, including readings, assignments, lesson plans, and more. Use the buttons below to filter resources by their **Literacy Domain/Subdomain** and **Resource Type**, or search for specific keywords across the resources. Check out our [Student Showcase]({{site.baseurl}}/student-showcase) to see how these resources have been implemented in the classroom.

<div class="help-banner" style="justify-content: center; font-size: 0.95em;">
  <i class="fa-regular fa-circle-question"></i> New to the toolkit? Learn more about our <a href="../literacy-domains/">literacy domains</a> of data advocacy and the different <a href="../resource-types/" style="color: #d32f2f; text-decoration: none; border-radius: 2px; transition: background 0.2s;" onmouseover="this.style.backgroundColor='#fdeaea'" onmouseout="this.style.backgroundColor=''">types of teaching resources.</a>
</div>

<!-- Domain Filter Section -->
<div class="filter-section mb-4">
  <h3 style="font-weight: 400;">Literacy Domains</h3>
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
  <!--
  <button class="reset-btn" data-reset="domain">
    Show All Domains
  </button>
  -->
</div>

<!-- Subdomain Filter Section (Hidden by default) -->
<div id="subdomain-section" class="filter-section mb-4" style="display: none;">
  <div style="text-align: center;">
    <h4 style="font-weight: 400;">Literacy Subdomains</h4>
    <div class="button-grid subdomain-grid">
      <!-- Populated dynamically by JavaScript -->
    </div>
  </div>
</div>

<!-- Resource Type Filter Section -->

<div class="filter-section mb-4">
  <h3 style="font-weight: 400;">Resource Types</h3>
  <div class="button-grid resource-grid">
    {% assign resources = site.data.cards.resources %}
    {% for resource in resources %}
    <button class="filter-btn resource-btn" data-filter="resource" data-value="{{ resource.name }}">
      <i class="{{ resource.icon }}"></i>
      {{ resource.name }}
    </button>
    {% endfor %}
  </div>
  <!-- uncomment to add a button to reset the filter
  <button class="reset-btn" data-reset="resource">
    Show All Resources
  </button>
  -->
</div>

<!-- Search Section -->
<div class="search-section mb-4">
  <h3 style="font-weight: 400;">Search Resources</h3>
  <div class="search-container">
    <input type="text" id="search-input" placeholder="Search resources...">
    <button id="search-btn" class="search-btn">Search</button>
    <button id="clear-search-btn" class="search-btn">Clear Search</button>
  </div>
</div>

<!-- Clear All Filters Button -->
<div class="filter-section mb-4">
  <button class="reset-btn" data-reset="all">
    <sl-icon name="arrow-clockwise"></sl-icon> Reset filters to show all resources
  </button>
</div>

---

<!-- Card List Section -->
<center>
<h2 style="font-weight: 400;">Filtered Resources (<span id="resource-count"></span>):</h2>
<p class="text-muted">
    <i>Click on card to access full resource</i></p>
</center>

{% assign domain_order = site.data.cards.domains %}
{% assign subdomain_order = site.data.cards.subdomains %}

<div id="card-list" style="margin-top: 20px;">
  {% for domain in domain_order %}
    {% for subdomain in subdomain_order %}
      {% assign cards = site.cards | where: "domain", domain | where: "subdomain", subdomain | sort: "title" %}
      {% for card in cards %}
        {% if card.title and card.teaser %}
          <div class="card-wrapper" onclick="window.location='{{ card.url | relative_url }}';" style="cursor: pointer;">
            <div class="card {% if card.inline == false %}hoverable{% endif %}" 
                 data-resource="{{ card.resource }}"
                 data-domain="{{ card.domain | join: ',' }}"
                 data-subdomain="{{ card.subdomain | join: ',' }}" style="margin-top: 10px;">
              {% assign resource = site.data.cards.resources | where: "name", card.resource | first %}
              <div class="row no-gutters">
                <div class="team">
                  <div class="card-body">
                    <h5 class="card-title"><i class="{{ resource.icon | default: 'fas fa-file' }}"></i>&nbsp;&nbsp; {{ card.title }}</h5>
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
                    <p class="card-text">
                      {% assign words = card.teaser | default: '' | number_of_words %}
                      {% if words > 150 %}
                        {% assign teaser_words = card.teaser | split: ' ' | slice: 0, 150 | join: ' ' %}
                        {{ teaser_words }} <span class="read-more">[Read More]</span>
                      {% else %}
                        {{ card.teaser }}
                      {% endif %}
                    </p>
                    {% if card.keywords.size > 0 %}
                      <!--<p class="card-text test-muted keyword"><small>Keywords: {% for keyword in card.keywords %}<i class="fa-solid fa-hashtag fa-sm"></i>&nbsp;{{ keyword }}&nbsp;&nbsp;{% endfor %}</small></p>-->
                      <p class="card-text keyword"><small><i class="fa-solid fa-tag"></i> Keywords: <span class="keywords-list">
                        {% for keyword in card.keywords %}
                          {{ keyword -}}
                          {% unless forloop.last %}, {% endunless %}
                        {% endfor %}
                      </span></small></p>
                    {% endif %}
                    <hr class="solid">
                    <p class="card-text">
                      {% assign domain_array = card.domain %}
                      <small class="test-muted resource"><i class="{{ resource.icon | default: 'fas fa-file' }}"></i>&nbsp; Resource: <span style="font-weight: 400;">{{ card.resource }}</span>&nbsp;&nbsp;//&nbsp;&nbsp;</small>
                      <small class="test-muted domain"><i class="fa-solid fa-network-wired"></i>&nbsp; Domain:
                        {% for d in domain_array %}
                          {% unless forloop.last %}
                            <a href="{{ site.url }}{{ site.baseurl }}/{{ d | downcase | replace: ' ', '-' }}" onclick="event.stopPropagation();">{{ d }}</a>,&nbsp;
                          {% else %}
                            <a href="{{ site.url }}{{ site.baseurl }}/{{ d | downcase | replace: ' ', '-' }}" onclick="event.stopPropagation();">{{ d }}</a>&nbsp;&nbsp;//&nbsp;&nbsp;
                          {% endunless %}
                        {% endfor %}
                      </small>
                      {% assign subdomain_array = card.subdomain %}
                      <small class="test-muted subdomain"><i class="fa-solid fa-sitemap"></i>&nbsp; Subdomain:
                        {% for sub in subdomain_array %}
                          {% unless forloop.last %}
                            <span style="font-weight: 400;">{{ sub }},&nbsp;</span>    {% else %}
                            <span style="font-weight: 400;">{{ sub }}</span>
                          {% endunless %}
                        {% endfor %}
                      </small><br>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        {% endif %}
      {% endfor %}
    {% endfor %}
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

    // Reset buttons (including new all-clear functionality)
    document.querySelectorAll('.reset-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        if (btn.dataset.reset === 'all') {
          this.clearAllFilters();
        } else {
          this.handleReset(btn.dataset.reset);
        }
      });
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
    let visibleCount = 0;
    
    cards.forEach(card => {
      const resourceType = card.dataset.resource;
      const domains = card.dataset.domain.split(',');
      const subdomains = card.dataset.subdomain.split(',');
      const cardText = card.textContent.toLowerCase();

      const resourceMatch = !this.state.resource || resourceType === this.state.resource;
      const domainMatch = !this.state.domain || domains.includes(this.state.domain);
      const subdomainMatch = !this.state.subdomain || subdomains.includes(this.state.subdomain);
      const searchMatch = !this.state.searchQuery || cardText.includes(this.state.searchQuery);

      const isVisible = resourceMatch && domainMatch && subdomainMatch && searchMatch;
      card.style.display = isVisible ? 'block' : 'none';
      
      if (isVisible) {
        visibleCount++;
      }
  });
  // Update just the number in the span
  document.getElementById('resource-count').textContent = visibleCount;
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

  clearAllFilters() {
    // Reset all state
    this.state = {
      resource: null,
      domain: null,
      subdomain: null,
      searchQuery: ''
    };
    
    // Remove all active classes from filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.classList.remove('active');
    });
    
    // Hide subdomain section
    document.getElementById('subdomain-section').style.display = 'none';
    
    // Clear search input
    const searchInput = document.getElementById('search-input');
    searchInput.value = '';
    
    // Re-filter cards to show all
    this.filterCards();
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  new ToolkitFilter();
});
</script>
