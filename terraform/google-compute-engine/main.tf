resource "google_compute_instance" "default" {
  count        = 3
  name         = "migrate-node-prod-${count.index+1}"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

#   tags = ["foo", "bar"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      labels = {
        my_label = "value"
      }
    }
  }

  // Local SSD disk
  scratch_disk {
    interface = "SCSI"
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

#   metadata_startup_script = "gsutil cp gs://bucket/* desktop do windows"

}