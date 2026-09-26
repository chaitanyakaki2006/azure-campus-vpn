# Services and Resources Required

## Azure Services

| Service / Resource | Purpose |
|---|---|
| Azure Virtual Network (VNet) | Provides the private network environment for Azure resources |
| GatewaySubnet | Dedicated subnet required for Azure VPN Gateway |
| Azure VPN Gateway | Establishes the Site-to-Site VPN connection |
| Public IP Address | Provides a public endpoint for the VPN Gateway |
| Local Network Gateway | Represents the campus network and VPN device in Azure |
| Site-to-Site VPN Connection | Connects the Azure VPN Gateway with the campus router |
| Azure Virtual Machine | Used as an optional cloud-side resource for connectivity testing |

## Networking Components

| Component | Purpose |
|---|---|
| Campus Router | Acts as the on-premises VPN endpoint |
| Campus Network | Contains campus servers and client systems |
| IPsec | Provides encrypted communication through the VPN tunnel |
| IKE | Negotiates security parameters between VPN endpoints |
| Routing | Ensures correct traffic flow between campus and Azure |

## Essential Resources

- Azure Virtual Network
- GatewaySubnet
- Azure VPN Gateway
- Public IP Address
- Local Network Gateway
- Site-to-Site VPN Connection
- Campus Router
- IKE/IPsec configuration
- Routing configuration

## Optional Resources

- Azure Virtual Machine
- Application Server
- Monitoring and Logging

## Purpose

These services and networking components work together to provide
secure hybrid connectivity between the campus on-premises network
and resources hosted in Azure.
