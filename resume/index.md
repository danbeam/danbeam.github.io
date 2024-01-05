---
title: Dan Beam's Resumé
---

## Education

B.S., Computer Science - [CSU-Fullerton](http://fullerton.edu) (2005 - 2009)<br>
M.S., Computer Science - [CSU-Fullerton](http://fullerton.edu) (2009 - on leave)

## Skills

<div class="rating" data-rate="5">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  JavaScript, TypeScript, technical design/leadership
</div>

<div class="rating" data-rate="4">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  Node.js, parsers, ASTs, linters, codemods
</div>

<div class="rating" data-rate="4">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  HTML, CSS, browsers, general web frontend
</div>

<div class="rating" data-rate="3.5">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  C++
</div>

<div class="rating" data-rate="3">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  Python, React, SQL
</div>

## Experience

### Staff Software Engineer @ [Airbnb](https://airbnb.com) (Nov 2020 - Present)

I’m a senior individual contributor / technical leader at Airbnb.

#### Web Platform (Aug 2021 - Present)

I'm currently on the Web Platform team, which supports things critical to web development at Airbnb like:
- continuous integration
- browser support
- in-house frameworks
- experimentation
- web development tooling
- linting
- testing

Lately I've been leading both the

- Observability squad
  - structured logging (Thrift schemas)
  - unstructured logging (Datadog metrics)
  - error reporting (via Bugsnag, previously Sentry)
  - alerting (via an in-house system to create Datadog / Grafana monitors)

- Experimentation squad
  - we implemented and maintain the complex (A/B testing) and simple (on & off switch) systems to launch features at Airbnb without needing to redeploy code

I previously led the Unit Testing squad in which I:

- helped strategically rethink testing at Airbnb (3-5yr vision presented to CTO)
- rewrote thousands of tests (chai, sinon → jest and enzyme → @testing-library/react) to reduce technical debt (via jscodeshift codemods, contractors, and elbow grease)

#### Trust (Oct 2020 - Sep 2021)

I previously worked in the [Trust](https://airbnb.com/trust) org at Airbnb, which deals with e.g. anti-fraud, physical safety, bot detection, and user challenges and frictions (think recaptcha or texting a login code).

I was the web lead for an Airbnb-wide framework that manages risk detection and enforcement.  This framework is implemented with [React](https://reactjs.org/), [TypeScript](https://www.typescriptlang.org/), [GraphQL](https://graphql.org/), [Jest](https://jestjs.io/) / [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/), and previously [Redux](https://redux.js.org/) and [Enzyme](https://enzymejs.github.io/enzyme/).<sup>[1]</sup>

<sup>[1]</sup> I wouldn't call myself a master of any of these skills 😉.

In addition to web, I've also helped design, plan, track, and execute projects across all the frontend tech stacks this framework supports (i.e. desktop/mobile web, native Android + iOS).

I've also:
- designed & implemented funnel metrics + time spent to measure and optimize business critical flows
- acted as an oncall / handled business critical matters on urgent timelines
- furthered bot detection across Airbnb / helped Google solve recaptcha bugs (we found → they fixed → we verified)
- championed privacy, code quality, and technical direction + refactor
- volunteered as a frontend architecture interviewer
- created an org-wide, dynamic careers page to recruit technical talent

### Principal Engineer @ [Quibi](https://quibi.com) (Jan 2020 - Nov 2020)

Quibi was a mobile-first streaming app that launched in Apr 2020.  Quibi raised $1.75BN in funding as of Mar 2020, and launched with over 1 million users.

I joined 3 months before launch to lead their web efforts.

In parallel I:

- guided 2 contractors in creating / iterating on quibi.com, which is:
  - a set of value propositions to explain to folks why they might want to install / subscribe to quibi
  - a dynamically generated, automatically deployed catalog of Quibi's content (w/ SEO & AMP optimizations)
- individually created sites to integrate with partners like [T-Mobile](https://t-mobile.quibi.com) and [Walmart](https://offers.quibi.com/walmart) in order to increase top-of-funnel metrics (i.e. get more users).
- led the team that created Quibi's [Chromecast receiver](https://developers.google.com/cast/) (what's on the TV).

Quibi [announced its shutdown on Oct 21, 2020](https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f).

### Staff Software Engineer @ [Google](https://google.com) (Jul 2011 - Jan 2020)

#### [Chrome](https://google.com/chrome) (Oct 2018 - Jan 2020)

- Reskinned all of Chrome's web UIs myself for dark mode (e.g. Mac OS X Mojave, Win10)
- Led a team of 4 working on Chrome's desktop New Tab page team (super visible surface w/ tons of traffic)

#### [Assistant](https://assistant.google.com/) (Jun 2017 - Oct 2018)

Worked on the "higher-level" brains behind Google Home / "OK Google".

#### [Chrome](https://google.com/chrome) (Jul 2011 - Jun 2017)

Contributed to:
- New Tab page (v4: the one with apps on it, not doodles)
- Autofill / [requestAutocomplete](http://www.html5rocks.com/en/tutorials/forms/requestautocomplete/)

Uber tech lead for:
- Settings UI (team of ~19 over ~2.5y)
- History page (team of ~4)
- Extensions page (~3)
- Downloads page (~me)

Misc things:
- Whisper to disks (asking "Are you an SSD?")
- Trace what Chrome asks your disks ("Does that file exist?")
- Make Chrome better for folks with disabilities (a11y)
- Typechecked many thousands of lines of JavaScript continuously
- Contributed to [Polymer](https://www.polymer-project.org/1.0/)
- Presented at [Google I/O](https://www.youtube.com/watch?v=1M50AXPd0Tg)

### Web Software Engineer @ [Yahoo!](https://yahoo.com) (Jul 2010 – Jul 2011)

Helped refactor and "modernize" new version of Yahoo! News to a more central stack (using PHP, CSS, JavaScript). Additionally, harnessed my efficient/lazy hacker powers to create small tools and scripts used by many developers all throughout Yahoo!'s media dept.

Also helped refactor/add to a completely browser-based media player called Yahoo! Web Player. It's no longer maintained, but it played and recognize content on internal and external sites.

### Web Software Engineer @ [Ticketmaster](https://ticketmaster.com)/[Live Nation](https://livenation.com) (Mar 2010 – Jul 2010, contract)

Contractor, helping w/ London 2012 Olympics ticketing website.

I helped create and maintain a test automation system that basically acts a commit hook to run tests when developers check in changes (for continuous integration purposes). I wrote many of the functional tests to be used with this system. I also created a "browser lab" where QA and other developers can locally or remotely test client-side performance and compatibility of our sites across browsers and platforms.

I implemented security enhancements, fixed many functional and content bugs, thought up new features to yield better user experience, and was also involved in the requirements gathering and time estimation. I additionally authored or maintained a couple of small tools to help improve internal workflow and ease the lives of fellow developers and testers (like bookmarklets to do mundane tasks, enhancing of a remote deployment daemon). I also refactored and modularized the Olympics' client-side code to be more autonomous and extensible.

I also worked briefly on ticketmaster.com and livenation.com (which sneakily switched to Ticketmaster's stack after their merger). I made style changes, added enhancements, worked on feature migration and integration, and helped make sure these changes did not affect other sites on the same infrastructure (regression tested).

### Web Software Engineer @ [AEG](https://aegworldwide.com) (Jun 2009 – Mar 2010)

Worked for AEG on Staples Center and LA Live's websites.

Used mainly open source technologies in a very high-traffic, clustered environment.

Some domains I worked on:
- staplescenter.com
- grammymuseum.org
- homedepotcenter.com
- latennischamps.com
- nokiatheatrelalive.com
- aegliveme.com
- anaheimarena.com

Some websites I ripped apart and put back together:
- lalive.com
- savethegrunt.com

I helped develop a custom CMS in PHP, PEAR / PECL, and MySQL. I helped on the frontend via UI feature work in HTML/CSS/JS/jQuery, learned the wonders of Apache's mod_rewrite, and did some security and performance analysis. I ended up fixing issues systemic to all of AEG's websites dealing with XSS, SQL injection, and/or arbitrary execution exploits.

### Web Software Engineer @ [Mt. San Antonio College](https://www.mtsac.edu) (Jun 2007 – Jun 2009)

Part of a team of 3 that developed, designed, and administered mtsac.edu. I was also lead programmer for all server-side (PHP/MySQL) and client-side (Javascript) scripting, responsible for almost all interactive features as well as a homepage redesign.

### Software Engineering @ [Central Desktop](https://en.wikipedia.org/wiki/Central_Desktop) (Aug 2008 – Dec 2008, intern)

I worked in a fast-paced Agile/Scrum environment for a collaborative business mgmt tool (centraldesktop.com). I was responsible for fixing bugs, adding features, giving input (during scrum planning), and helping develop a site with over hundreds of thousands of users worldwide.

### Advertising Webmaster @ [The Daily Titan](https://dailytitan.com) (Jun 2005 – Jul 2007)

Sole developer of main domain, dailytitan.com, and various subdomains: history.dailytitan.com, archive.dailytitan.com (they even won awards!).

I also created an online yearbook / community for CSU Fullerton while with The Daily Titan (titanyearbook.com), as well as posted the online news items and ads in early morning hours.
