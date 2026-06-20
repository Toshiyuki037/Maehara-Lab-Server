# Maehara Lab Server

A Raspberry Pi 5 home lab server featuring NVMe SSD boot, battery-backed UPS protection, and a Waveshare e-paper dashboard for real-time system monitoring.

<div align="center">
  <table>
    <tr>
      <td><img src="screenshots/IMG1943.jpg" width="250" height="250" style="object-fit: cover;"></td>
      <td><img src="screenshots/IMG1942.jpg" width="250" height="250" style="object-fit: cover;"></td>
    </tr>
    <tr>
      <td><img src="screenshots/IMG1941.jpg" width="250" height="250" style="object-fit: cover;"></td>
      <td><img src="screenshots/IMG1940.jpg" width="250" height="250" style="object-fit: cover;"></td>
    </tr>
  </table>
</div>

## Hardware

* Raspberry Pi 5 (8GB)
* PCIe M.2 NVMe HAT+
* 256GB NVMe SSD
* Geekworm X1200 UPS HAT
* Waveshare 2.13" E-Ink Display HAT V4

## Features

* NVMe SSD boot
* UPS-backed power protection
* Automatic safe shutdown
* Persistent e-paper dashboard
* Headless SSH operation
* Local engineering lab storage

## Dashboard

The e-paper dashboard displays:

* WiFi Status
* UPS Status
* SSD Status
* CPU Temperature
* RAM Usage
* Disk Usage
* IP Address

The dashboard launches automatically at boot through a systemd service.

## Services

### UPS Daemon

```bash
systemctl status x120x_upsd
```

### E-Paper Dashboard

```bash
systemctl status epaper-status.service
```

Restart dashboard:

```bash
sudo systemctl restart epaper-status.service
```

## Repository Structure

```text
maehara-lab-server/
├── epaper_status.py
├── README.md
├── systemd/
│   ├── epaper-status.service
│   └── x120x_upsd.service
└── screenshots/
```

## Future Development

* Engineering project storage
* Research data management
* FPGA project archive
* KiCad library repository
* CAD file backup system
* Internal Git services
* Home lab monitoring

## Current Status

Operational and running on NVMe storage with UPS protection and automated e-paper monitoring.
# Maehara Lab Server

A Raspberry Pi 5 home lab server featuring NVMe SSD boot, battery-backed UPS protection, and a Waveshare e-paper dashboard for real-time system monitoring.

## Hardware

* Raspberry Pi 5 (8GB)
* PCIe M.2 NVMe HAT+
* 256GB NVMe SSD
* Geekworm X1200 UPS HAT
* Waveshare 2.13" E-Ink Display HAT V4

## Features

* NVMe SSD boot
* UPS-backed power protection
* Automatic safe shutdown
* Persistent e-paper dashboard
* Headless SSH operation
* Local engineering lab storage

## Dashboard

The e-paper dashboard displays:

* WiFi Status
* UPS Status
* SSD Status
* CPU Temperature
* RAM Usage
* Disk Usage
* IP Address

The dashboard launches automatically at boot through a systemd service.

## Services

### UPS Daemon

```bash
systemctl status x120x_upsd
```

### E-Paper Dashboard

```bash
systemctl status epaper-status.service
```

Restart dashboard:

```bash
sudo systemctl restart epaper-status.service
```

## Repository Structure

```text
maehara-lab-server/
├── epaper_status.py
├── README.md
├── systemd/
│   ├── epaper-status.service
│   └── x120x_upsd.service
└── screenshots/
```

## Future Development

* Engineering project storage
* Research data management
* FPGA project archive
* KiCad library repository
* CAD file backup system
* Internal Git services
* Home lab monitoring

## Current Status

Operational and running on NVMe storage with UPS protection and automated e-paper monitoring.
