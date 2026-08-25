---
layout: page
title: AI-Driven IoT Development
permalink: /iot/
---

<p class="terminal-prompt">pi@iot-lab:~$ whoami</p>

<p>
  A Raspberry Pi 4 runs four Claude agents that autonomously develop
  firmware for two ESP32-S3 boards. Tasks arrive over Telegram; every
  change ships as a reviewed, tested GitHub pull request.
</p>

<p>
  Test-driven development is enforced structurally, not by convention —
  a Reviewer agent can hard-reject a merge, and nothing counts as done
  until it's verified on real, physical hardware.
</p>

<p class="terminal-prompt">pi@iot-lab:~$ cat ./current_focus</p>

<div class="terminal-listing">
  <div class="tl-row tl-active">
    <span class="tl-type tl-status-active">done</span>
    <span class="tl-name">Phase 8 — Message integrity &amp; encryption</span>
    <span class="tl-desc">CRC-32, sequence numbers, cross-board replay detection, TLS over MQTT, battery-optimized operation. Merged. → <a href="/iot/blog/">Blog</a></span>
  </div>
  <div class="tl-row">
    <span class="tl-type">next</span>
    <span class="tl-name">Phase 9 — Auth &amp; identity</span>
    <span class="tl-desc">PSK setup, HMAC-SHA256 signing, device identity tokens, key rotation</span>
  </div>
</div>

<p class="terminal-prompt">pi@iot-lab:~$ ps aux | grep agent</p>

<div class="terminal-listing">
  <div class="tl-row">
    <span class="tl-type">agent</span>
    <span class="tl-name">Orchestrator</span>
    <span class="tl-desc">Receives instructions over Telegram, routes work, merges PRs, reports back</span>
  </div>
  <div class="tl-row">
    <span class="tl-type">agent</span>
    <span class="tl-name">Coder</span>
    <span class="tl-desc">Writes firmware, opens PRs, never touches test files</span>
  </div>
  <div class="tl-row">
    <span class="tl-type">agent</span>
    <span class="tl-name">Reviewer</span>
    <span class="tl-desc">Checklist-based review with hard-reject authority — not just suggestions</span>
  </div>
  <div class="tl-row">
    <span class="tl-type">agent</span>
    <span class="tl-name">Tester</span>
    <span class="tl-desc">Flashes real hardware, captures serial output, asserts against test specs</span>
  </div>
</div>

<p class="terminal-prompt">pi@iot-lab:~$ ls ./navigate</p>

<div class="terminal-listing">
  <div class="tl-row"><span class="tl-type">dir</span><span class="tl-name"><a href="/iot/blog/">Blog</a></span><span class="tl-desc">The full write-up series, phase by phase</span></div>
  <div class="tl-row"><span class="tl-type">dir</span><span class="tl-name"><a href="/iot/tags/">Tags</a></span><span class="tl-desc">Browse IoT posts by topic</span></div>
  <div class="tl-row"><span class="tl-type">dir</span><span class="tl-name"><a href="/iot/evidence/">Evidence</a></span><span class="tl-desc">Full Telegram transcript — every claim in the series, sourced</span></div>
  <div class="tl-row"><span class="tl-type">dir</span><span class="tl-name"><a href="https://github.com/ondrejrollinger">GitHub</a></span><span class="tl-desc">Firmware repo, pull requests, decisions.md</span></div>
</div>

<p class="terminal-prompt terminal-prompt--dim">pi@iot-lab:~$ cat ./disclosure</p>
<p class="terminal-note terminal-note--dim">AI tools may assist with drafting and editing for clarity. Technical work, evidence selection, validation, and conclusions are mine.</p>
