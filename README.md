# Azure VPN Gateway Site-to-Site Tunnel to a Campus Router

## Project Overview

This project focuses on establishing secure Site-to-Site connectivity
between a campus on-premises network and an Azure Virtual Network
using Azure VPN Gateway.

The solution enables campus servers and Azure resources to communicate
securely through an encrypted IPsec VPN tunnel over the Internet.

## Problem Statement

Campus servers need secure and reliable communication with resources
hosted in Azure. A Site-to-Site VPN is proposed to provide private
connectivity between the campus network and Azure.

The project also addresses two important VPN connectivity challenges:

- IKE proposal mismatch
- Asymmetric routing

## Objectives

- Establish secure Site-to-Site VPN connectivity.
- Connect the campus network with an Azure Virtual Network.
- Configure compatible IKE and IPsec parameters.
- Ensure correct routing between campus and Azure.
- Detect and troubleshoot VPN connectivity failures.
- Support hybrid application communication.

## Proposed Architecture

```text
                    ┌──────────────────────────────┐
                    │          INTERNET            │
                    └──────────────┬───────────────┘
                                   │
                    IKEv2 / IPsec VPN Tunnel
                                   │
             ┌─────────────────────┴─────────────────────┐
             │                                           │
             ▼                                           ▼
┌────────────────────────────┐             ┌────────────────────────────┐
│  SIMULATED CAMPUS NETWORK  │             │        AZURE CLOUD         │
│                            │             │                            │
│  Network: 10.20.0.0/24     │             │  VNet: 10.1.0.0/16         │
│                            │             │                            │
│  ┌──────────────────────┐  │             │  ┌──────────────────────┐  │
│  │ Campus VPN Router VM │  │             │  │  Azure VPN Gateway   │  │
│  │                      │  │             │  │                      │  │
│  │ Ubuntu 24.04         │  │◄═══════════►│  │ Route-based          │  │
│  │ strongSwan           │  │  IKEv2/IPsec│  │ VpnGw2AZ             │  │
│  │                      │  │             │  │ 4.217.131.246        │  │
│  │ Private IP:          │  │             │  └──────────┬───────────┘  │
│  │ 10.20.0.4            │  │             │             │              │
│  │ Public IP:           │  │             │      GatewaySubnet         │
│  │ 20.41.123.138        │  │             │      10.1.255.0/27         │
│  └──────────┬───────────┘  │             │             │              │
│             │              │             │             ▼              │
│             ▼              │             │  ┌──────────────────────┐  │
│  ┌──────────────────────┐  │             │  │   Azure Test VM      │  │
│  │ Campus Network       │  │             │  │                      │  │
│  │ 10.20.0.0/24         │  │             │  │ Private IP: 10.1.0.4 │  │
│  └──────────────────────┘  │             │  └──────────────────────┘  │
└────────────────────────────┘             └────────────────────────────┘
             │                                           │
             │                                           │
             └─────────────────┬─────────────────────────┘
                               │
                               ▼
                  ┌────────────────────────────┐
                  │    CAMPUSVPN GUARDIAN      │
                  │                            │
                  │  • IKE Status              │
                  │  • IPsec Status            │
                  │  • Traffic Counters        │
                  │  • Outbound XFRM Policy    │
                  │  • Inbound XFRM Policy     │
                  │  • VPN Diagnosis           │
                  │  • Recommendations         │
                  └─────────────┬──────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ localhost:5000  │
                       │ Flask Dashboard │
                       └─────────────────┘
