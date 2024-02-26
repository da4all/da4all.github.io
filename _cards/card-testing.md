---
layout: page
inline: false
group: Assignment
domains: [ Understanding Data , Persuading With Data ]

title: Testing Page
description: Here is the citation for this card
lastname: Jane Doe

teaser: >
  [DESCRIPTION]

profile:
    name: "[TITLE]"
    group: Reading / Term / Assignment / Activity / Tutorial / Teaching Module / Dataset / Example of Data Advocacy
    domain: 
            <a href="../understanding-data/">Understanding Data</a>
            <a href="../processing-data/">Processing Data</a>
            <a href="../persuading-with-data/">Persuading with Data</a>
    subdomain: 
            <a href="../defining-data/">Defining Data</a>
            <a href="../critiquing-data/">Critiquing Data</a>
            <a href="../acting-ethically-with-data/">Acting Ethically with Data</a>
            <a href="../linking-data-and-justice/">Linking Data and Justice</a>
            <a href="../collecting-data/">Collecting Data</a>
            <a href="../organizing-and-cleaning-data/">Organizing and Cleaning Data</a>
            <a href="../analyzing-and-drawing-insights-from-data/">Analyzing and Drawing Insights from Data</a>
            <a href="../storing-and-preserving-data/">Storing and Preserving Data</a>
            <a href="../appealing-with-data/">Appealing with Data</a>
            <a href="../visualizing-data/">Visualizing Data</a>
            <a href="../mapping-data/">Mapping Data</a>
            <a href="../telling-multi-modal-stories-with-data/">Telling Multi-Modal Stories with Data</a>
    source: "https://markcarrigan.net/2016/09/12/the-history-of-data-as-rhetoric/"
    author: [AUTHOR FULL NAME]
    license: [LICENSE TYPE HERE / CC BY / CC BY-SA / CC BY-NC / CC-BY-NA-SA / CC BY-ND / CC BY-NC-ND / CC0 ]
    align: right

---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.5.2/cdn/themes/light.css" />
<script type="module" src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.5.2/cdn/shoelace.js" ></script>

## General notes

I think we can do quite a bit with defining metadata for individual cards in teh frontmatter alongside site-wide variables and metadata (or at least lists of things like tags for all cards) within a .yaml file in the ``_data`` folder (currently I made a file called ``cards.yml`` there). Then we can access adn manipulate this metadata using Liquid, which allows for logic statements, loops, etc. I've outlined a couple of examples below.

## List of domains for this card: 

If a. particular card falls within multiple domains/sub-domains. This is listing out the domains based on the frontmatter:

<ul>
{% for domain in page.domain %}
  <li>{{ domain }}</li>
{% endfor %}
</ul>

## Checking consistency of metadata

We can also do a quality control check to make sure that the domain that someone writes in a specific card is spelled correctly and lines up with one of the site-wide domains we've defined separately in the _data folder:

<!-- note: just using one domain for simplicity, but could check for both -->

{% assign current_domain = page.domain[0] %}
{% assign list_domains = site.data.cards.domains %}
{% assign is_allowed = false %}

{% if list_domains contains current_domain %}
  {% assign is_allowed = true %}
{% endif %}

{% if is_allowed %}
  <p>The tag '{{ current_domain }}' IS an allowed domain.</p>
{% else %}
  <p>The tag '{{ current_domain }}' is NOT an allowed domain.</p>
{% endif %}

## Filter other cards based on domains

{% assign current_domain = page.domain[0] %}

This list is generated using Liquid to get a list of cards that have the same domain name as this card ( ie. ``{{ current_domain }}`` ). Here is a list of their card-specific ``title`` linked to their card-specific ``url``:

<ul>
{% for card in site.cards %}
  {% if card.domain contains current_domain %}
    <li><a href="{{ card.url | relative_url }}">{{ card.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>





<div>
  <center>
  <sl-button-group label="Alignment">
  <sl-button href=" {{ page.source }} ">[BUTTON TEXT GOES HERE]</sl-button>
  </sl-button-group>
</center>
</div>

<br>
