## NODE SERVERS ##

resource "google_compute_address" "node_static" {
  name = "node-ipv4-address-${count.index+1}"
  address_type  = "INTERNAL"
  count = var.node_number
}

resource "google_compute_instance" "node_server" {
  count        = var.node_number
  name         = "migrate-node-${var.env}-${count.index+1}"
  machine_type = var.node_machine_type
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "windows-cloud/windows-2019"
      size = var.node_disk_size
      type = "pd-ssd"
    }
  }

  service_account {
    scopes = ["cloud-platform"]
  }

  network_interface {
    network = "default"
    network_ip = google_compute_address.node_static[count.index].address

    access_config {
      //
    }
  }


}

