---
layout: page
permalink: /testing/
title: Testing
description:
nav: false
nav_rank: 8
---

## Testing 76

<div class="tag-category-list">
  <ul class="p-0 m-0">
    {% for tag in site.display_tags %}
      <li>
        <i class="fa-solid fa-hashtag fa-sm"></i> <a href="{{ tag | slugify | prepend: '/blog/tag/' | relative_url }}">{{ tag }}</a>
      </li>
      {% unless forloop.last %}
        <p>&bull;</p>
      {% endunless %}
    {% endfor %}
  </ul>
</div>

<select id="keyword-filter">
  <option value="all">All Keywords</option>
  {% for card in site.cards %}
    {% for keyword in card.keywords %}
      <option value="{{ keyword }}">{{ keyword }}</option>
    {% endfor %}
  {% endfor %}
</select>

<div id="card-list" style="margin-top: 20px;">
  {% for card in site.cards %}
    <div class="card {% if card.inline == false %}hoverable{% endif %}" style="margin-bottom: 20px; display: none;" data-domain="{{ card.domain }}" data-subdomain="{{ card.subdomain }}">
      <div class="row no-gutters">
        <div class="team">
          <div class="card-body">
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <h5 class="card-title"><i class="fas fa-file"></i>&nbsp;&nbsp; {{ card.title }}</h5></a>
            <p class="card-text"><small class="test-muted">{% if card.profile.date %}<i class="fa-solid fa-calendar"></i>&nbsp; Date: {{ card.profile.date | replace: '<br />', ', ' }}{% endif %}
              {% if card.profile.date and card.profile.author %}&nbsp;&nbsp;//&nbsp;&nbsp;{% endif %}
              {% if card.profile.author %}<i class="fa-solid fa-user"></i>&nbsp; Author: {{ card.profile.author | replace: '<br />', ', ' }}{% endif %}</small></p>
            {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
              <p class="card-text">
                {% assign words = card.teaser | number_of_words %}
                {% if words > 150 %}
                  {% assign teaser_words = card.teaser | split: ' ' | slice: 0, 150 | join: ' ' %}
                  {{ teaser_words }} <small class="test-muted"><a href="{{ card.url | relative_url }}">&nbsp;<b><u>[...]</u></b></a> </small></p>
                {% else %}
                  {{ card.teaser }}</p>
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
              <small class="test-muted resource"><i class="fas fa-file"></i>&nbsp; Type of Resource: {{ card.resource }}</small><br>
              <small class="test-muted keyword">{% for keyword in card.keywords %}<i class="fa-solid fa-hashtag fa-sm"></i>&nbsp;{{ keyword }}&nbsp;&nbsp;{% endfor %}</small>
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
  const keywordFilter = document.getElementById('keyword-filter');
  const cards = document.querySelectorAll('.card');

  // Define a mapping of subdomains to corresponding domains
  const subdomainToDomain = {
    'All': 'All',
    'Defining Data': 'Understanding Data',
    'Critiquing Data': 'Understanding Data',
    'Acting Ethically with Data': 'Understanding Data',
    'Linking Data and Justice': 'Understanding Data',
    'Collecting Data': 'Processing Data',
    'Organizing and Cleaning Data': 'Processing Data',
    'Analyzing and Drawing Insights from Data': 'Processing Data',
    'Storing and Preserving Data': 'Processing Data',
    'Appealing with Data': 'Persuading with Data',
    'Visualizing Data': 'Persuading with Data',
    'Mapping Data': 'Persuading with Data',
    'Telling Multi-Modal Stories with Data': 'Persuading with Data'
  };

  function filterCards() {
    const selectedDomain = domainFilter.value;
    const selectedSubdomain = subdomainFilter.value;
    const selectedResource = resourceFilter.value;
    const selectedKeyword = keywordFilter.value;

    cards.forEach(card => {
      const domain = card.getAttribute('data-domain'); // Get domain from data attribute
      const subdomain = card.getAttribute('data-subdomain'); // Get subdomain from data attribute
      const resource = card.querySelector('.resource').textContent.trim().replace('Type of Resource: ', ''); 
      const keywords = Array.from(card.querySelectorAll('.keyword')).map(elem => elem.textContent.trim());

      const domainMatch = selectedDomain === 'all' || domain === selectedDomain;
      const subdomainMatch = selectedSubdomain === 'all' || subdomain === selectedSubdomain;
      const resourceMatch = selectedResource === 'all' || resource === selectedResource;
      const keywordMatch = selectedKeyword === 'all' || keywords.includes(selectedKeyword);

      if (domainMatch && subdomainMatch && resourceMatch && keywordMatch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  domainFilter.addEventListener('change', filterCards);
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
  keywordFilter.addEventListener('change', filterCards);

  // Initial filtering when the page loads
  filterCards();
});
</script>
