---
title: Dan Beam's Résumé
---

<style>
h3 { cursor: pointer; }
</style>

## Education

B.S., Computer Science - [CSU-Fullerton](http://fullerton.edu) (2005 - 2009)<br>
M.S., Computer Science - [CSU-Fullerton](http://fullerton.edu) (2009 - on leave)

## Skills

<div class="rating" data-rate="5">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  JavaScript, TypeScript, technical design/leadership
</div>

<div class="rating" data-rate="4.5">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  Node.js, parsers, ASTs, linters, codemods
</div>

<div class="rating" data-rate="4">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  React, HTML, CSS, browsers, general web frontend
</div>

<div class="rating" data-rate="3.5">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  C++
</div>

<div class="rating" data-rate="3">
  <i class="star-1">★</i><i class="star-2">★</i><i class="star-3">★</i><i class="star-4">★</i><i class="star-5">★</i>
  Python, SQL
</div>

## Experience

### Senior Staff Software Engineer @ [Affirm](https://www.affirm.com/) (July 2025 - present)

I am the frontend (FE) area tech lead ([A]TL) for the Purchasing Experience (PX) organization at Affirm, which is made up of:

- ~25 frontend engineers that I lead directly
- ~25 backend (BE) engineers that I correspond with regularly / sometimes lead or influence (some are fullstack)
- organized into 6 remote fullstack (FE + BE) teams of ~9 across the US and Europe (~50 total)

I report to the Director of this org and support each of these teams in varying ways depending on their needs, including:

- attending standups, sprint plannings/retros, and team times when possible
- reviewing all frontend designs and a majority of all FE pull requests (PRs) for risk assessment and technical quality
- attending many topic-specific and cross-functional syncs
- recurring 1:1s with tech leads, managers, and other ICs

PX owns:

- [the JavaScript SDK](https://docs.affirm.com/developers/v1.1-developer-reference/docs/affirmjs-quick-guide) that allows hundreds of thousands of merchants (e.g. Walmart, Amazon, Target) to integrate Affirm with their online store
- ["As low as $$/mth with Affirm" promotional UI](https://docs.affirm.com/developers/docs/set-up-promotional-messaging) shown on merchant websites
- a [prequalification UI](https://docs.affirm.com/developers/docs/about-promotional-messaging-and-prequalification#prequalification) to show potential borrowers their purchasing power
- the [checkout experience](https://docs.affirm.com/developers/docs/affirm-checkout-overview) when a user selects Affirm to pay at checkout
  - initiating a checkout and establishing context / authenticating (note: there are 100+ variations of our checkout)
  - fetching, showing, and selecting loan terms
  - fetching, creating, and saving new payment instruments (taking, validating, and saving payment info e.g. credit card or account number)
  - responding to various "step up" mechanisms in which further information (or sometimes payment) is required to proceed with the transaction
  - confirming the checkout after decisions have been made and the loan has been underwritten, passing back info to the merchant
 
The general technical stack is:

- TypeScript (and some legacy JavaScript) in a monorepo with mostly [Buildkite](https://buildkite.com/) for CI/CD
- React and many custom NPM packages (e.g. a components library) we maintain
- Kotlin [backend-for-frontends (BFFs)](https://en.wikipedia.org/wiki/Front_end_and_back_end#API) and legacy Python backends
- various [REST](https://en.wikipedia.org/wiki/REST) and [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) clients (e.g. [gRPC](https://grpc.io/) + [protobuf](https://protobuf.dev/))

Additionally, I take part in various company-wide efforts to:

- shape and improve the future of web development at Affirm dealing with: service-oriented architectures, observability, design systems, and sharing code between React Native & web
- produce technical guidance on good web development practices: which lint rules and styleguide[s] to use, documentation format (easy to comment/discover, readable by AI), and automated enforcement of this guidance
- evaluate whether software engineers should be promoted from Senior to Staff level (promo committee)

### Staff Software Engineer @ [Airbnb](https://airbnb.com) (Nov 2020 - July 2025)

I was senior individual contributor / technical leader at Airbnb.

#### On Trip (Aug 2024 - July 2025)

I previously led the frontend engineering for the "Trips" page, rewriting the UI from the ground up for [services](https://news.airbnb.com/airbnb-2025-summer-release/): a whole new offering in addition to stays and experiences.  The Trips UI helps folks track their booking and get to their stay/experience/service (e.g. provides the address a certain time before the start) and generally deals with the user's experience after booking but before their booking has ended and ties in deeply into reservation details, altering reservations, inviting others ("co-travelers"), etc.  It also provides users with smartlock PINs and upsells experiences in the location while on stays and other things while on the trip.

I worked as the most senior IC on a team of 10 cross-functionally with many designers, product managers, and engineers from other teams to ship on a fairly agressive timeline (6mo) for a very visible, critical surface.

Technologically, Trips uses (on web):

- [GraphQL](https://graphql.org/)
- [TypeScript](https://www.typescriptlang.org/)
- [React](https://react.dev/)
- a bunch of internal components and frameworks (shared design systems components, graphql infra, etc.)

and gets data from [Viaduct](https://github.com/airbnb/viaduct), a Kotlin/Java graphql backend.

I personally wrote a lot of the code for the web UI, lead other frontend contributors, and indentified problems and unblocked.  For example, there was a complicated state graph across multiple platforms (iOS, Android, web) mostly based on time before booking start/end.  Everybody on the team was using different terms, constantly re-explaining things, and folks were basically writing as many bugs as they were fixing.  I created a model for a unified "trip stage", sought feedback from all stakeholders, and implemented the first proof of concept in web code and with supporting documentation (this also drastically affected how designs were done in Figma).  This model significantly reduced miscommunication and complexity while creating a common vocabulary.  I also worked various data modeling problems with backend folks to provide the frontend with the right set of data in the format that would be the most useful and performant.

The new Trips UI launched on all platforms in as part of the CEO keynote for the [Summer 2025 release](https://news.airbnb.com/airbnb-2025-summer-release/).

#### Web Platform (Aug 2021 - Aug 2024)

I was previously on the Web Platform team.

They support things critical to web development at Airbnb like:
- continuous integration
- browser support
- in-house frameworks
- experimentation
- web development tooling
- linting
- testing

I previously led these squads (team groups):

- Observability
  - structured logging (Thrift schemas)
  - unstructured logging (Datadog metrics)
  - error reporting (via Bugsnag, previously Sentry)
  - alerting (via an in-house system to create Datadog / Grafana monitors)

- Experimentation
  - we implemented and maintain the complex (A/B testing) and simple (on & off switch) systems to launch features at Airbnb without needing to redeploy code

- Unit Testing
  - helped strategically rethink testing at Airbnb (3-5yr vision presented to CTO)
  - rewrote thousands of tests (chai, sinon → jest and enzyme → @testing-library/react) to reduce technical debt (via jscodeshift codemods, contractors, and elbow grease)

I also participated in an oncall rotation, being one of the first to be paged if something web-related were to fail at Airbnb (across the whole company).

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
