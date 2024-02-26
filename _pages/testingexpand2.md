---
layout: page
permalink: /testingexpand2/
title: Testing Expandable Cards 2
description: 
nav: false
nav_rank: 8
---

{% assign domains = site.data.cards.domains %}

<div class="card-container">
{% for domain in domains %}
  <h2>{{ domain }}</h2>
  {% for card in site.cards %}
    {% if card.domain == domain %}
      <div class="card">
        <div class="card-header">
          <h3 class="card-title">{{ card.title }}</h3>
          <button class="toggle-button">Expand</button>
        </div>
        <div class="card-content" style="display: none;">
          <p>
            {% if card.profile.author %}
              <small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }}</small><br>
            {% endif %}
            {% if card.teaser %}
              <p>{{ card.teaser }}</p>
            {% endif %}
            {% if card.profile.source %}
              <small class="test-muted"><i class="fas fa-link"></i> Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a></small>
            {% endif %}
          </p>
          <!-- Expanded content (replace iframe with Markdown content) -->
          <div class="expanded-content">
            {{ card.content }}
          </div>
        </div>
      </div>
    {% endif %}
  {% endfor %}
{% endfor %}
</div>

<script>
const toggleButtons = document.querySelectorAll('.toggle-button');

toggleButtons.forEach(button => {
  button.addEventListener('click', () => {
    const cardContent = button.closest('.card').querySelector('.card-content');
    cardContent.classList.toggle('expanded');
    button.textContent = cardContent.classList.contains('expanded') ? 'Collapse' : 'Expand';
  });
});

window.addEventListener('scroll', function() {
  const headers = document.querySelectorAll('.card-header');
  headers.forEach(header => {
    const rect = header.getBoundingClientRect();
    if (rect.top <= 0) {
      header.classList.add('sticky');
    } else {
      header.classList.remove('sticky');
    }
  });
});
</script>

<style>
.card-container {
  margin-bottom: 20px;
}

.card {
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.card-header.sticky {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: white;
}

.card-content .test-muted {
  font-size: 0.8em;
  margin-bottom: 5px;
}

.expanded-content {
  margin-top: 10px;
}

.toggle-button {
  margin-left: 10px;
}
</style>
