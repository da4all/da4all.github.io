---
layout: page
permalink: /resource-types/
title: Types of Resources
description:
nav: false
nav_order:
---

The [Data Advocacy For All Toolkit]({{site.baseurl}}/toolkit) is a curated collection of teaching resources designed to support data advocacy. These resources are organized under the following categories:

<div class="resource-grid">
  {% for resource in site.data.cards.resources %}
    <div class="resource-card">
      <i class="{{ resource.icon }}"></i>
      <h3 style="font-weight: 400;">{{ resource.name }}</h3>
      <p>{{ resource.description }}</p>
    </div>
  {% endfor %}
</div>

<style>
.resource-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin: 1.5rem 0;
}

@media (min-width: 700px) {
  .resource-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
.resource-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px hsla(0, 0.00%, 0.00%, 0.20);
  padding: 1.2rem;
  text-align: center;
  transition: box-shadow 0.2s;
}

.resource-card i {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  display: block;
}
</style>

<center>
  <sl-button variant="primary" size="large" outline href="../toolkit/"><sl-icon name="wrench-adjustable"></sl-icon> Go to the Toolkit</sl-button>
</center>
