---
layout: page
permalink: /testing3/
title: Testing 3
description: 
nav: false
nav_rank: 8
---

<style>
.card {
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.card-title {
  background-color: #f2f2f2;
  padding: 10px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  position: sticky;
  top: 0;
  z-index: 1;
}

.card-body {
  padding: 10px;
}

.card-content {
  display: none;
  padding: 10px;
}

.toggle-button {
  margin-top: 10px;
}
</style>

<div id="cards-container">
  {% assign cards = site.cards | sort: "title" %}
  
  {% for card in cards %}
    <div class="card">
      <h3 class="card-title">{{ card.title }}</h3>
      <div class="card-body">
        {% if card.profile.author %}
          <p><small class="test-muted">Author: {{ card.profile.author | replace: '<br />', ', ' }}</small></p>
        {% endif %}
        <p class="card-text">{{ card.teaser }}</p>
        <p class="card-text">
          {% if card.profile.source %}
            <small class="test-muted"><i class="fas fa-link"></i> Source: <a href="{{ card.profile.source }}">{{ card.profile.source | replace: '<br />', ', ' }}</a></small><br>
          {% endif %}
          <small class="test-muted domain">Domain: {{ card.domain }}</small><br>
          <small class="test-muted topic">Topic: {{ card.topic }}</small><br>
          <small class="test-muted group">Group: {{ card.group }}</small><br>
        </p>
        <button class="toggle-button">Expand</button>
        <div class="card-content">
          {{ card.content }}
          <button class="collapse-button">Collapse</button>
        </div>
      </div>
    </div>
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const toggleButtons = document.querySelectorAll('.toggle-button');
  const collapseButtons = document.querySelectorAll('.collapse-button');

  toggleButtons.forEach(button => {
    button.addEventListener('click', function() {
      const cardContent = this.parentElement.querySelector('.card-content');
      cardContent.style.display = 'block';
    });
  });

  collapseButtons.forEach(button => {
    button.addEventListener('click', function() {
      const cardContent = this.parentElement;
      cardContent.style.display = 'none';
    });
  });
});
</script>
