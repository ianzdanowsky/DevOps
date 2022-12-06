resource "google_compute_address" "mysql_static" {
  name = "mysql-ipv4-address"
  address_type  = "INTERNAL"
}

resource "google_compute_instance" "mysql_server" {
  name         = "migrate-mysql-${var.env}"
  machine_type = var.db_machine_type
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "windows-cloud/windows-2019"
      size = var.db_disk_size
      type = "pd-ssd"
    }
  }

  
  service_account {
    scopes = ["cloud-platform"]
  }

  network_interface {
    network = "default"
    network_ip = google_compute_address.mysql_static.address

    access_config {
      //
    }
  }

}