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

<div class="phase-grid">
  <div class="phase-grid-head">
    <div>status</div><div>#</div><div>phase</div><div>summary</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">00</div>
    <div class="phase-title">Network isolation</div>
    <div class="phase-desc">VLAN-isolated lab network, static DHCP by MAC, exit-gate verification before any firmware work began</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">01</div>
    <div class="phase-title">Pipeline bootstrap</div>
    <div class="phase-desc">Orchestrator/Coder/Reviewer/Tester roles, TDD enforcement, the adversarial test proving the Reviewer actually rejects bad code</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">02</div>
    <div class="phase-title">Structured logging</div>
    <div class="phase-desc">Event logging conventions, automated test reports, the board-identity assertion gap found and closed</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">03</div>
    <div class="phase-title">Sensors</div>
    <div class="phase-desc">BH1750 light, BMP280 pressure/temp, SH1106 OLED display on both boards</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">04</div>
    <div class="phase-title">WiFi &amp; UDP telemetry</div>
    <div class="phase-desc">WiFi connect reliability, UDP broadcast, AP/DHCP infrastructure fixes</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">05</div>
    <div class="phase-title">Reliable WiFi</div>
    <div class="phase-desc">Connection stability hardening, TCP soak testing across both boards</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">06</div>
    <div class="phase-title">MQTT</div>
    <div class="phase-desc">Bidirectional sensor data over MQTT, cross-board OLED integration</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">done</div>
    <div class="phase-num">07</div>
    <div class="phase-title">Power &amp; sleep</div>
    <div class="phase-desc">Deep sleep power management on both boards</div>
  </div>
  <div class="phase-row phase-row--active">
    <div class="phase-status">done</div>
    <div class="phase-num">08</div>
    <div class="phase-title">Message integrity &amp; encryption</div>
    <div class="phase-desc">CRC-32, sequence numbers, cross-board replay detection, TLS over MQTT, battery-optimized operation. Merged. → <a href="/iot/blog/">Blog</a></div>
  </div>
  <div class="phase-row phase-row--next">
    <div class="phase-status">next</div>
    <div class="phase-num">09</div>
    <div class="phase-title">Auth &amp; identity</div>
    <div class="phase-desc">PSK setup, HMAC-SHA256 signing, device identity tokens, key rotation</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">ahead</div>
    <div class="phase-num">10</div>
    <div class="phase-title">Cert management</div>
    <div class="phase-desc">Expiry monitoring, automated rotation, revocation</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">ahead</div>
    <div class="phase-num">11</div>
    <div class="phase-title">OTA updates</div>
    <div class="phase-desc">Signed binaries, rollback on boot failure, multi-device rollout</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">ahead</div>
    <div class="phase-num">12</div>
    <div class="phase-title">Resilience</div>
    <div class="phase-desc">Watchdog hardening, crash dumps, brownout detection, autonomous recovery</div>
  </div>
  <div class="phase-row">
    <div class="phase-status">ahead</div>
    <div class="phase-num">13</div>
    <div class="phase-title">Standalone deployment</div>
    <div class="phase-desc">Factory-flashable image, WiFi/cert provisioning, OLED-based status reporting</div>
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
  <div class="tl-row"><span class="tl-type">dir</span><span class="tl-name"><a href="https://github.com/ondrejrollinger">GitHub</a></span><span class="tl-desc">Firmware repo, pull requests, decisions.md</span></div>
</div>

<p class="terminal-prompt terminal-prompt--dim">pi@iot-lab:~$ cat ./disclosure</p>
<p class="terminal-note terminal-note--dim">AI tools may assist with drafting and editing for clarity. Technical work, evidence selection, validation, and conclusions are mine.</p>
