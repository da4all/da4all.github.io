---
layout: page
permalink: /keywords/
title: Keywords
description:
nav: false
nav_order: 5
---

## Unique Keywords and Frequencies

{% assign all_keywords = "" | split: "" %}
{% for card in site.cards %}
{% if card.keywords %}
{% for keyword in card.keywords %}
{% assign keyword_clean = keyword | strip %}
{% unless keyword_clean == "" %}
{% assign all_keywords = all_keywords | push: keyword_clean %}
{% endunless %}
{% endfor %}
{% endif %}
{% endfor %}

{% assign keyword_names = "" | split: "" %}
{% for keyword in all_keywords %}
{% unless keyword_names contains keyword %}
{% assign keyword_names = keyword_names | push: keyword %}
{% endunless %}
{% endfor %}

{% assign keyword_names = keyword_names | sort %}

{% assign keyword_table = "" | split: "" %}
{% for name in keyword_names %}
{% assign count = 0 %}
{% for keyword in all_keywords %}
{% if keyword == name %}
{% assign count = count | plus: 1 %}
{% endif %}
{% endfor %}
{% assign row = name | append: "," | append: count %}
{% assign keyword_table = keyword_table | push: row %}
{% endfor %}

{% assign sorted_keyword_table = keyword_table | sort %}

Total keywords: {{ sorted_keyword_table | size }}

List of all keywords and their frequencies across all cards.

<table style="width: 500px;">
  <tr>
    <th style="width: 70%;">Keyword</th>
    <th style="width: 30%;">Count</th>
  </tr>
  {% for row in sorted_keyword_table %}
    {% assign parts = row | split: "," %}
    <tr>
      <td style="padding: 2px 8px;">{{ parts[0] }}</td>
      <td style="text-align: center; padding: 2px 8px;">{{ parts[1] }}</td>
    </tr>
  {% endfor %}
</table>
