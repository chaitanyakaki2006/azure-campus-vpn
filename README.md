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
                 INTERNET
                    |
             IPsec / IKE VPN
                    |
        +-----------+-----------+
        |                       |
+-------v--------+       +------v-----------+
| Campus Router  |       | Azure VPN Gateway|
+-------+--------+       +------+-----------+
        |                       |
+-------v--------+       +------v-----------+
| Campus Network|       |    Azure VNet    |
| 192.168.1.0/24|       |    10.0.0.0/16   |
+----------------+       +------+-----------+
                                |
                         +------v------+
                         |  Azure VM   |
                         +-------------+
