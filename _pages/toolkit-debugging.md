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
  <h4>Card File Validation:</h4>

{% assign processed_files = site.cards | map: "path" %}
{% assign all_files = site.static_files | where_exp: "file", "file.path contains '/_cards/'" %}

  <h5>Files in _cards folder not being processed:</h5>
  <ul>
  {% for file in all_files %}
    {% unless processed_files contains file.path %}
      <li style="color: #d73a49;">{{ file.path }} - Not being processed</li>
    {% endunless %}
  {% endfor %}
  </ul>

  <h5>Processed Card Files with Issues:</h5>
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
    
    {% if has_issues %}
      <li style="color: #d73a49;">
        <strong>{{ card.path }}</strong><br>
        Issues found:
        <ul>
          {% for issue in issues %}
            <li>{{ issue }}</li>
          {% endfor %}
        </ul>
      </li>
    {% endif %}
  {% endfor %}
  </ul>

  <h5>Summary Counts:</h5>
  <ul>
    <li>Total files in _cards folder: {{ all_files | size }}</li>
    <li>Files being processed by Jekyll: {{ site.cards | size }}</li>
    <li>Files not being processed: {{ all_files | size | minus: site.cards | size }}</li>
  </ul>
</div>
