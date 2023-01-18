# Gardener Shoot Cluster Pulumi Component
[![Security Scan](https://github.com/phoenix1480/pulumi-gardener-shoot-cluster/actions/workflows/security-scan.yml/badge.svg?branch=main)](https://github.com/phoenix1480/pulumi-gardener-shoot-cluster/actions/workflows/security-scan.yml)
[![Code Quality Scan](https://github.com/phoenix1480/pulumi-gardener-shoot-cluster/actions/workflows/code-quality-scan.yml/badge.svg)](https://github.com/phoenix1480/pulumi-gardener-shoot-cluster/actions/workflows/code-quality-scan.yml)


The Gardener shoot cluster component lets you create, deploy, and manage [Gardener Kubernetes](https://gardener.cloud/) shoot clusters for multiple infrastructure providers.

## Supported Providers

[Infrastructure Providers](https://gardener.cloud/docs/extensions/infrastructure-extensions/) include:

- Alicloud
- Azure
- AWS
- Equinix Metal
- GCP
- Openstack
- vSphere

## Prerequisites

In order to deploy a Gardener shoot cluster, the following are required:

- Gardener Control Plane API Endpoint
- Gardener Project Name
- Gardener Project Credentials
- Gardener Shoot Cluster Manifest

## References

- [Official Gardener project on GitHub](https://github.com/gardener)
- [Gardener Shoot Cluster Manifest](https://github.com/gardener/gardener/blob/master/example/90-shoot.yaml)
