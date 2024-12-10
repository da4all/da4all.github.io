---
layout: page
permalink: /toolkit-debugging/
title: Toolkit Debugging
description:
nav: true
nav_order: 5
---

Welcome to the Data Advocacy for All Toolkit! This is a curated collection of teaching resources designed to support data advocacy, including readings, assignments, lesson plans, and more. Use the buttons below to filter resources by their <code>Resource Type</code> and <code style="background-color: rgba(0, 54, 159, 0.1); color: #00369f; padding: 2px 4px; border-radius: 4px;">Literacy Domain/Subdomain</code>, or search for specific topics or keywords across the resources.

<!-- Debug section -->
<script>
const fileList = air-pollution-and-public-health-in-south-bronx.md
amcha-initiative.md
analysis-of-fish-pharm-visualization.md
analysis-of-roosevelt-reelection-flyer.md
attending-to-the-cultures-of-data-science-work.md
black-health-in-america.md
care-principles-for-indigenous-data-governance.md
caregiving-is-real-work.md
chai-importance-of-data-cleaning.md
classifying-household-goods.md
collect-analyze-imagine-teach.md
collecting-thick-data.md
correlation-crump-reading-and-guidelines-for-discussion.md
create-an-original-data-visualization.md
creating-digital-research-notebooks.md
critical-data-studies.md
critique-an-infographic.md
data-advocacy-op-ed.md
data-advocacy-projects-addressing-gun-violence.md
data-advocacy.md
data-and-indigenous-knowledge.md
data-biography.md
data-cleaning.md
data-ethics-society.md
data-ethics-unveiled.md
data-ethics.md
data-feminism-book.md
data-feminism.md
data-governance.md
data-harm-record.md
data-harms.md
data-justice.md
data-management-and-sharing.md
data-management-tutorials.md
data-registry.md
data-repository.md
data-sharing-and-management-snafu-in-3-short-acts.md
data-sovereignty.md
data-stewardship.md
data-storytelling-effectively-tell-a-story-with-data.md
data-storytelling-presentation-assignment.md
data.md
dataset-documentation-assignment.md
dear-data.md
deconstructing-a-published-map.md
demonstrating-causation-slide-deck.md
deon-data-ethics-checklist-for-data-scientists.md
elite-institution-cognitive-disorder.md
ethics-of-managing-people's-data.md
evaluating-statistical-claims-slide-deck.md
exploring-data.md
exploring-distributions-and-central-tendency.md
exploring-distributions-and-measures-of-variation.md
fair-guiding-principles.md
fair-principles.md
fbi-2021-hate-crimes-dataset-basic-analysis.md
formal-critical-reflection-defining-data.md
foundational-principles-for-good-data-management-and-stewardship.md
framing-statistics-slide-deck.md
from-data-visualizations-to-data-stories.md
game-based-research-data-management-training.md
gapminder-world-health-chart.md
getting-started-with-data-for-advocacy-slide-deck.md
guide-to-choosing-a-digital-repository.md
guide-to-social-science-data-preparation-and-archiving.md
history-of-data-as-rhetoric.md
how-to-create-a-data-visualization-slide-deck.md
improve-it-and-prove-it.md
individual-data-advocacy-project.md
interview-with-catherine-dignazio.md
introduction-to-data-data-harms-and-data-advocacy.md
introduction-to-data-ethics.md
introduction-to-data-management-best-practices-for-research.md
introduction-to-data-visualization-videos.md
limits-of-data.md
managing-and-sharing-data.md
many-ways-to-write-a-statistic.md
map-design-critical-cartography.md
mapping-broadband-health-in-america.md
mapping-police-violence.md
mapping-technology-society.md
maps-GIS-social-change.md
maps-as-advocacy-slide-deck.md
maps-health-advocacy.md
of-oaths-and-checklists.md
philadelphia-african-american-consensus-1847.md
police-stops-mapping-exercise.md
practical-tips-for-ethical-data-sharing.md
primer-for-researchers-on-how-to-manage-data.md
principles-for-advancing-equitable-data-practice.md
raw-data-is-an-oxymoron.md
research-data-management-and-sharing.md
research-data-management-workbook.md
rhetorical-analysis-of-data-advocacy-projects.md
rhetorical-data-studies-approach.md
rhetorical-data-studies.md
rhetorical-numbers.md
seven-principles-of-data-feminism.md
shafer-and-zhang-introductory-statistics-basic-definitions.md
six-steps-to-decolonizing-data.md
snopes-fact-checking-article-assignment-sequence.md
sovereign-bodies-institute.md
splc-hate-map.md
strangers-in-the-dataset.md
strategies-for-analyzing-and-composing-data-stories.md
student-debt-mapping-exercise.md
swastika-counter-project.md
telling-counter-stories-with-data.md
the-point-of-collection.md
thick-data-slide-deck.md
thick-data-vs-big-data.md
three-creative-ways-to-fix-fashion's-waste-problem.md
to-visualize-or-not-slide-deck.md
truth-about-human-population-decline.md
virulent-hate-project.md
what-does-critical-data-studies-look-like-and-why-do-we-care.md
what-gets-counted-counts.md
what-is-a-digital-registry.md
what-is-data-an-activity.md
what-is-data-defintions-and-examples.md
what-is-data-governance-and-why-does-it-matter.md
what-is-data-slidedeck.md
what-where-and-how-of-data.md
why-big-data-needs-thick-data.md
world-happiness-report-2023.md
world-happiness-report-critical-analysis.md
write-your-own-data-advocacy-values-statement.md`.split('\n');

console.log("Total number of files:", fileList.length);

// Look for potential problem files (very short names or unusual patterns)
const suspiciousFiles = fileList.filter(file => {
    return file.length < 10 || // Very short names
           file === 'data.md' || // Single word names
           !file.includes('-'); // Files without hyphens
});

console.log("\nPotential problem files:");
suspiciousFiles.forEach(file => console.log(file));

</script>

<!--
<blockquote class="block-warning">
<p><i class="fa-regular fa-circle-question"></i>New to the toolkit? Learn about our <b><a href="../resource-types/">types of resources</a></b> and <b><a href="../literacy-domains/">literacy domains & subdomains</a></b>.</p>
</blockquote>
-->

<div class="help-banner" style="justify-content: center">
  <i class="fa-regular fa-circle-question"></i> New to the toolkit? Learn more about our different <a href="../resource-types/">types of resources</a> and <a href="../literacy-domains/">literacy domains</a> of data advocacy.
</div>

<!-- Resource Type Filter Section -->

<div class="filter-section mb-4">
  <h3>Resource Types</h3>
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

<!-- Domain Filter Section -->
<div class="filter-section mb-4">
  <h3>Literacy Domains</h3>
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
    <h4>Literacy Subdomains</h4>
    <div class="button-grid subdomain-grid">
      <!-- Populated dynamically by JavaScript -->
    </div>
  </div>
</div>

<!-- Search Section -->
<div class="search-section mb-4">
  <h3>Search Resources</h3>
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
<h2>Filtered Resources (<span id="resource-count"></span>):</h2>
<p class="text-muted">
    <i>Click on card to access full resource</i></p>
</center>

<div id="card-list" style="margin-top: 20px;">
  {% assign cards = site.cards | sort: "title" %}
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
                  <hr class="solid">
                  <p class="card-text test-muted keyword"><small>Keywords: {% for keyword in card.keywords %}<i class="fa-solid fa-hashtag fa-sm"></i>&nbsp;{{ keyword }}&nbsp;&nbsp;{% endfor %}</small></p>
                {% endif %}
                {% if card.metadata.source or card.metadata.license %}
                  <hr class="solid">
                {% endif %}
                <p class="card-text">
                  {% if card.metadata.source %}
                    <small class="test-muted"><i class="fas fa-link"></i> Source: <a href="{{ card.metadata.source }}" onclick="event.stopPropagation();">{{ card.metadata.source | replace: '<br />', ', ' }}</a></small>
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
                  {% assign domain_array = card.domain %}
                  <small class="test-muted resource"><i class="{{ resource.icon | default: 'fas fa-file' }}"></i>&nbsp; Type of Resource: {{ card.resource }}&nbsp;&nbsp;//&nbsp;&nbsp;</small>
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
                        {{ sub }},&nbsp;
                      {% else %}
                        {{ sub }}
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
