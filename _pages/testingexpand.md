---
layout: page
permalink: /testingexpand/
title: Testing Expandable Cards 
description: 
nav: false
nav_rank: 8
---

{% assign domains = site.data.cards.domains %}

{% for domain in domains %}
  <h2>{{ domain }}</h2>
  <div class="card-container">
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
  </div>
{% endfor %}

<script>
  const toggleButtons = document.querySelectorAll('.toggle-button');

  toggleButtons.forEach(button => {
    button.addEventListener('click', () => {
      const cardContent = button.closest('.card').querySelector('.card-content');
      cardContent.style.display = cardContent.style.display === 'none' ? 'block' : 'none';
      button.textContent = cardContent.style.display === 'none' ? 'Expand' : 'Collapse';
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

  .card-content .test-muted {
    font-size: 0.8em;
    margin-bottom: 5px;
  }

  .expanded-content {
    margin-top: 10px;
  }
</style>
