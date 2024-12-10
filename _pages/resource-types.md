---
layout: page
permalink: /resource-types/
title: Types of Resources
description:
nav: false
nav_order:
---

The [Data Advocacy For All Toolkit]({{site.baseurl}}/toolkit) is a curated collection of teaching resources designed to support data advocacy. These resources are organized under the following categories:

<ul>
  {% for resource in site.data.cards.resources %}
  <li><b><i class="{{ resource.icon }}"></i> {{ resource.name }}:</b> 
    {% case resource.name %}
    {% when 'Term' %}
    Concepts that are key to each subdomain along with brief definitions and identification of source. Most of the concepts are discussed in the subdomain's open-access readings.
    {% when 'Reading' %}
    Open-access sources that introduce students to important frameworks, concepts, practices, and strategies for doing data advocacy. A list of closed access content is also included on some occasions.
    {% when 'Assignment' %}
    Formal work that gives students opportunity to learn, practice, and reflect on their experiences with data advocacy. These assignments can also be used to assess student learning in relation to each data literacy domain and subdomain.
    {% when 'Activity' %}
    Open-access lessons developed by the Data Advocacy for All team and other authors. Activities vary in length and scope, that can be implemented in the classroom to help students hone their abilities to work with data in several literacy domains and subdomains.
    {% when 'Tutorial' %}
    Step-by-step instructions for using various open-access digital tools to work with data. Most tutorials rely on minimal computing, so no previous computer experience is required.
    {% when 'Lesson Plan' %}
    A structured collection of resources to help students gain experience with a particular subdomain. This may include readings, glossary, activities, tutorials, etc.
    {% when 'Example Project' %}
    A collection of projects and advocacy movements that utilize data advocacy to bring about social change. Some of these examples are referenced in activities, assignments, modules, and tutorials, while others are simply listed to further model for data advocacy.
    {% when 'Slides' %}
    Open-access slide decks curated by Data Advocacy for All team members to assist the teaching of data advocacy and help hone students hone the multiple literacies needed to do data advocacy is ethical, responsible, and persuasive ways. Many slide decks correspond with specific activities and assignments listed under the various literacy subdomains.
    {% endcase %}
  </li>
  <br>
  {% endfor %}
</ul>

<center>
  <sl-button variant="primary" size="large" outline href="../toolkit/"><sl-icon name="wrench-adjustable"></sl-icon> Go to the Toolkit</sl-button>
</center>
