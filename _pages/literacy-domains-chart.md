---
layout: page
permalink: /literacy-domains-chart/
title: Literacy Domains Chart
description:
nav: false
---

<style>
:root {
  --domain-color: #00369f;
  --subdomain-btn-color: #00369f;
  --subdomain-btn-active-background: #e8f0fe;
}

.filter-section {
  margin-bottom: 2rem;
  text-align: center;
  align-items: center;
}

.button-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1rem;
  width: 100%;
  align-items: center;
}

.domain-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.filter-btn {
  background-color: white;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
  font-weight: 500;
  width: 100%; /* Set a consistent width for all buttons */
}

.domain-btn{
  background-color: var(--domain-color);
  color: white;
}

.subdomain-grid {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  width: 90%;
  align-items: center;
}

.subdomain-btn {
  background-color: white;
  color: var(--subdomain-btn-color);
  border-color: var(--subdomain-btn-color);
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
  font-weight: 500;
  width: 100%; /* Set a consistent width for all buttons */
}

.domain-btn:hover, .domain-btn.hover {
  background-color: var(--domain-color);
  transform: scale(1.04);
  color: white;
}

.domain-btn.active {
  background-color: var(--domain-color);
  transform: scale(1.02);
}

.subdomain-btn:hover, .subdomain-btn.hover {
  background-color: var(--subdomain-btn-active-background);
  color: var(--subdomain-btn-color);
  transform: scale(1.04);
  opacity: 1;
}

.subdomain-btn.active {
  opacity: 1;
  transform: scale(1.1);
  color: var(--subdomain-btn-color);
  background-color: var(--subdomain-btn-active-background);
}
</style>

<div class="filter-section">
    <div class="button-grid">
      <!-- Main Domains -->
      <div class="domain-column" data-domain="understanding">
        <button class="filter-btn domain-btn" data-domain="understanding">
          <i class="fas fa-brain"></i>
          Understanding Data
        </button>
        <div class="subdomain-grid">
          <button class="filter-btn subdomain-btn" data-parent="understanding">Defining Data</button>
          <button class="filter-btn subdomain-btn" data-parent="understanding">Critiquing Data</button>
          <button class="filter-btn subdomain-btn" data-parent="understanding">Acting Ethically with Data</button>
          <button class="filter-btn subdomain-btn" data-parent="understanding">Thinking Rhetorically about Data</button>
        </div>
      </div>

      <div class="domain-column" data-domain="processing">
        <button class="filter-btn domain-btn" data-domain="processing">
          <i class="fas fa-cogs"></i>
          Processing Data
        </button>
        <div class="subdomain-grid">
          <button class="filter-btn subdomain-btn" data-parent="processing">Collecting Data</button>
          <button class="filter-btn subdomain-btn" data-parent="processing">Preparing Data</button>
          <button class="filter-btn subdomain-btn" data-parent="processing">Analyzing Data</button>
          <button class="filter-btn subdomain-btn" data-parent="processing">Storing and Preserving Data</button>
        </div>
      </div>

      <div class="domain-column" data-domain="persuading">
        <button class="filter-btn domain-btn" data-domain="persuading">
          <i class="fas fa-chart-line"></i>
          Persuading with Data
        </button>
        <div class="subdomain-grid">
          <button class="filter-btn subdomain-btn" data-parent="persuading">Making Claims with Data</button>
          <button class="filter-btn subdomain-btn" data-parent="persuading">Visualizing Data</button>
          <button class="filter-btn subdomain-btn" data-parent="persuading">Mapping Data</button>
          <button class="filter-btn subdomain-btn" data-parent="persuading">Telling Stories with Data</button>
        </div>
      </div>
    </div>

  </div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Hover functionality for domain buttons
  document.querySelectorAll('.domain-btn').forEach(button => {
    button.addEventListener('mouseenter', function() {
      const domain = this.dataset.domain;
      this.classList.add('hover');
      document.querySelectorAll(`.subdomain-btn[data-parent="${domain}"]`)
        .forEach(sub => sub.classList.add('hover'));
    });

    button.addEventListener('mouseleave', function() {
      const domain = this.dataset.domain;
      this.classList.remove('hover');
      document.querySelectorAll(`.subdomain-btn[data-parent="${domain}"]`)
        .forEach(sub => sub.classList.remove('hover'));
    });
  });

  // Hover functionality for subdomain buttons
  document.querySelectorAll('.subdomain-btn').forEach(button => {
    button.addEventListener('mouseenter', function() {
      const parentDomain = this.dataset.parent;
      document.querySelector(`.domain-btn[data-domain="${parentDomain}"]`)
        .classList.add('hover');
      document.querySelectorAll(`.subdomain-btn[data-parent="${parentDomain}"]`)
        .forEach(sub => sub.classList.add('hover'));
    });

    button.addEventListener('mouseleave', function() {
      const parentDomain = this.dataset.parent;
      document.querySelector(`.domain-btn[data-domain="${parentDomain}"]`)
        .classList.remove('hover');
      document.querySelectorAll(`.subdomain-btn[data-parent="${parentDomain}"]`)
        .forEach(sub => sub.classList.remove('hover'));
    });
  });
});
</script>
