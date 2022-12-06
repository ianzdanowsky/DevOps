resource "google_compute_address" "platform_static" {
  name = "platform-ipv4-address"
  address_type  = "INTERNAL"
}

resource "google_compute_instance" "platform_server" {
  name         = "migrate-platform-${var.env}"
  machine_type = var.platform_machine_type
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "windows-cloud/windows-2019"
      size = var.platform_disk_size
      type = "pd-ssd"
    }
  }
  
  service_account {
    scopes = ["cloud-platform"]
  }

  network_interface {
    network = "default"
    network_ip = google_compute_address.platform_static.address

    access_config {
      //
    }
  }

}