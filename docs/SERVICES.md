# Services and Resources Required

# Services and Resources Required

## Azure Services

| Service / Resource | Purpose |
|---|---|
| **Azure Virtual Network (VNet)** | Provides the private network environment for Azure resources |
| **GatewaySubnet** | Dedicated subnet required for the Azure VPN Gateway |
| **Azure VPN Gateway** | Establishes the Site-to-Site VPN connection with the simulated campus router |
| **Public IP Address** | Provides the public endpoint for the Azure VPN Gateway |
| **Local Network Gateway** | Represents the simulated campus VPN router and its network address space in Azure |
| **Site-to-Site VPN Connection** | Connects the Azure VPN Gateway with the simulated campus router |
| **Azure Virtual Machine** | Used as the Azure-side resource for connectivity testing |

## Networking Components

| Component | Purpose |
|---|---|
| **Simulated Campus VPN Router** | Acts as the campus-side VPN endpoint using Ubuntu and strongSwan |
| **Simulated Campus Network** | Represents the campus network using the `10.20.0.0/24` address space |
| **IPsec** | Provides encrypted communication between the simulated campus network and Azure |
| **IKEv2** | Negotiates security parameters between the VPN endpoints |
| **strongSwan** | Establishes and manages the IKEv2/IPsec VPN tunnel on the simulated campus router |
| **Routing** | Ensures correct traffic flow between the simulated campus network and Azure |
| **XFRM Policies** | Define and validate inbound and outbound IPsec traffic policies |
| **CampusVPN Guardian** | Monitors VPN status, traffic, IPsec policies, and provides diagnostic recommendations |

## Essential Resources

- Azure Virtual Network
- GatewaySubnet
- Azure VPN Gateway
- Public IP Address
- Local Network Gateway
- Site-to-Site VPN Connection
- Simulated Campus VPN Router
- strongSwan
- IKEv2/IPsec configuration
- Routing configuration
- CampusVPN Guardian

## Optional Resources

- Azure Virtual Machine
- Connectivity Testing
- Monitoring and Logging

## Purpose

These services and networking components work together to provide secure hybrid connectivity between the **simulated campus network** and resources hosted in **Azure**. The solution uses **IKEv2/IPsec** to establish the Site-to-Site VPN tunnel and **CampusVPN Guardian** to monitor the VPN state, validate traffic policies, and provide diagnostic recommendations for IKE/IPsec and routing issues.
