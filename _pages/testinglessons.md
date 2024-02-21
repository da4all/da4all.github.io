---
layout: page
permalink: /testing/
title: Testing
description: 
nav: false
nav_rank: 8
---

<div id="filter-options">
  <label for="domain-filter">Domain:</label>
  <select id="domain-filter">
    <option value="all">All</option>
    <option value="Understanding Data">Understanding Data</option>
    <option value="Processing Data">Processing Data</option>
    <option value="Persuading with Data">Persuading with Data</option>
  </select>
  
  <label for="topic-filter">Topic:</label>
  <select id="topic-filter">
    <option value="all">All</option>
    <option value="Defining Data">Defining Data</option>
    <option value="Critiquing Data">Critiquing Data</option>
    <!-- Add other topics here -->
  </select>
  
  <label for="group-filter">Group:</label>
  <select id="group-filter">
    <option value="all">All</option>
    <option value="Reading">Reading</option>
    <option value="Assignment">Assignment</option>
    <!-- Add other groups here -->
  </select>
</div>

<div id="card-list">

{% assign cards = site.cards | sort: "title" %}

{% for card in cards %}

<p>
    <div class="card {% if card.inline == false %}hoverable{% endif %}">
        <div class="row no-gutters">
            <div class="team">
		    <div class="card-body">
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <h5 class="card-title">{{ card.profile.name }}</h5></a>
			    <p class="card-text">{% if card.profile.author %}<small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }} </small><br>{% endif %}</p>
			    {% if card.inline == false %}<a href="{{ card.url | relative_url }}">{% endif %}
				    <p class="card-text">{{ card.teaser }}</p></a>
			    <p class="card-text">
			    <div style="height:1px;font-size:1px;">&nbsp;</div>
			    {% if card.profile.source %}<small class="test-muted"><i class="fas fa-link"></i>  Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a> </small><br>{% endif %} 
			    <small class="test-muted"><i class="fas fa-square-poll-vertical"></i>  Data Literacy: {{ card.profile.domain | replace: '<br />', ', ' }} &nbsp;&nbsp;►&nbsp; Subdomain: {{ card.profile.subdomain | replace: '<br />', ', ' }} <br></small>
			    <small class="test-muted"><i class="fas fa-table-columns"></i>  Resource Type: {{ card.profile.group | replace: '<br />', ', ' }} </small><br>
                    </p>
                </div>
            </div>
        </div>
    </div>
</p>

{% endfor %}

<div style="height:1px;font-size:1px;">&nbsp;</div>

<br>

</details>

<div style="height:5px;font-size:1px;">&nbsp;</div>

</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const domainFilter = document.getElementById('domain-filter');
    const topicFilter = document.getElementById('topic-filter');
    const groupFilter = document.getElementById('group-filter');
    const cards = document.querySelectorAll('.card');
    
    function filterCards() {
      const selectedDomain = domainFilter.value;
      const selectedTopic = topicFilter.value;
      const selectedGroup = groupFilter.value;
      
      cards.forEach(card => {
        const domain = card.querySelector('.domain').textContent.trim();
        const topic = card.querySelector('.topic').textContent.trim();
        const group = card.querySelector('.group').textContent.trim();
        
        const domainMatch = selectedDomain === 'all' || domain === selectedDomain;
        const topicMatch = selectedTopic === 'all' || topic === selectedTopic;
        const groupMatch = selectedGroup === 'all' || group === selectedGroup;
        
        if (domainMatch && topicMatch && groupMatch) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
    
    domainFilter.addEventListener('change', filterCards);
    topicFilter.addEventListener('change', filterCards);
    groupFilter.addEventListener('change', filterCards);
  });
</script>
