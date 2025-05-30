---
layout: page
permalink: /toolkit-testing/
title: Toolkit Testing
description:
nav: false
nav_order: 5
---

[Original]({{base.url}}/curricularsite/toolkit/)

[Testing Option 1]({{base.url}}/curricularsite/toolkit-testing-1/)

[Testing Option 2]({{base.url}}/curricularsite/toolkit-testing-2/)

[Testing Option 3]({{base.url}}/curricularsite/toolkit-testing-3/)

## Outputting keywords

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
{% assign keyword_counts = "" | split: "" %}

{% for keyword in all_keywords %}
{% unless keyword_names contains keyword %}
{% assign keyword_names = keyword_names | push: keyword %}
{% endunless %}
{% endfor %}

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

{% assign sorted_keyword_table = keyword_table | sort: "last" | reverse %}

<table>
  <tr>
    <th>Keyword</th>
    <th>Count</th>
  </tr>
  {% for row in sorted_keyword_table %}
    {% assign parts = row | split: "," %}
    <tr>
      <td>{{ parts[0] }}</td>
      <td>{{ parts[1] }}</td>
    </tr>
  {% endfor %}
</table>

<ul>
{% for card in site.cards %}
  <li>
    {{ card.title }}:
    {% if card.keywords %}
      {% for keyword in card.keywords %}
        [{{ keyword }}]
      {% endfor %}
    {% else %}
      (no keywords)
    {% endif %}
  </li>
{% endfor %}
</ul>
