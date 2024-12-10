---
layout: page
permalink: /toolkit-debugging/
title: Toolkit Debugging
description:
nav: true
nav_order: 5
---

<!-- Card File Validation -->
<div style="background: #fff3e6; padding: 20px; margin: 20px 0; border-radius: 8px;">
  <h4>Card Collection Analysis:</h4>
  
  <h5>Resource Type Analysis:</h5>
  <ul>
  {% assign valid_resources = "Term,Reading,Assignment,Activity,Tutorial,Lesson Plan,Example Project,Slides" | split: "," %}
  {% for card in site.cards %}
    {% unless valid_resources contains card.resource %}
      <li style="color: #d73a49;">
        <strong>{{ card.path }}</strong> - Invalid resource type: "{{ card.resource }}"
      </li>
    {% endunless %}
  {% endfor %}
  </ul>

  <h5>Collection Debug Information:</h5>
  <ul>
    <li>Collection directory: {{ site.collections.cards.directory }}</li>
    <li>Collection files (site.cards): {{ site.cards | size }}</li>
    <li>Collection label: {{ site.collections.cards.label }}</li>
    <li>Collection relative directory: {{ site.collections.cards.relative_directory }}</li>
  </ul>

  <h5>Files By Domain:</h5>
  {% assign all_domains = site.cards | map: "domain" | uniq | compact %}
  <ul>
  {% for domain in all_domains %}
    <li>{{ domain }}: {{ site.cards | where: "domain", domain | size }} files</li>
  {% endfor %}
  </ul>

  <h5>Processed Card Files Analysis:</h5>
  <ul>
  {% for card in site.cards %}
    {% assign has_issues = false %}
    {% assign issues = "" | split: "" %}
    
    {% unless card.layout == "card" %}
      {% assign has_issues = true %}
      {% assign issues = issues | push: "Invalid layout (should be 'card')" %}
    {% endunless %}
    
    {% unless card.title %}
      {% assign has_issues = true %}
      {% assign issues = issues | push: "Missing title" %}
    {% endunless %}
    
    {% unless card.teaser %}
      {% assign has_issues = true %}
      {% assign issues = issues | push: "Missing teaser" %}
    {% endunless %}
    
    {% unless card.resource %}
      {% assign has_issues = true %}
      {% assign issues = issues | push: "Missing resource type" %}
    {% endunless %}
    
    {% unless card.domain %}
      {% assign has_issues = true %}
      {% assign issues = issues | push: "Missing domain" %}
    {% endunless %}
    
    {% unless card.subdomain %}
      {% assign has_issues = true %}
      {% assign issues = issues | push: "Missing subdomain" %}
    {% endunless %}
    
    <li style="{% if has_issues %}color: #d73a49;{% endif %}">
      <strong>{{ card.path }}</strong>
      {% if has_issues %}
        <br>Issues found:
        <ul>
          {% for issue in issues %}
            <li>{{ issue }}</li>
          {% endfor %}
        </ul>
      {% else %}
        - Valid card
      {% endif %}
    </li>
  {% endfor %}
  </ul>

  <h5>Raw Collection Data:</h5>
  <pre style="background: #f6f8fa; padding: 10px; border-radius: 4px; overflow-x: auto;">
    Collection Files Count: {{ site.cards | size }}
    Valid Cards Count: {{ site.cards | where: "layout", "card" | size }}
  </pre>
</div>
