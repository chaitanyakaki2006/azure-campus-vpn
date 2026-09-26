# Project Abstract

The project aims to establish a secure Site-to-Site VPN connection
between a campus on-premises network and an Azure Virtual Network
using Azure VPN Gateway.

The solution enables secure communication between campus servers and
cloud-based resources through an encrypted IPsec VPN tunnel over the
Internet.

The campus router acts as the on-premises VPN endpoint, while Azure
VPN Gateway acts as the cloud-side VPN endpoint. IKE is used to
negotiate security parameters, while IPsec provides secure
communication between the two networks.

The project focuses on two important VPN connectivity challenges:
IKE proposal mismatches and asymmetric routing. Compatible IKE/IPsec
parameters are configured to establish the tunnel, while appropriate
routing is configured to ensure that outbound and return traffic
follow the intended VPN path.

The proposed solution supports hybrid applications where application
components or servers can operate across campus and Azure environments.
Connectivity and VPN status can be verified through network and
connection testing.
