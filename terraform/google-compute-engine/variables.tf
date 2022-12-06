########################
#### MAIN VARIABLES ###
########################

variable "project_id" {
  type    = string
}

variable "env" {
    type = string
    default = "dev"
}


########################
#### NODES VARIABLES ###
########################

variable "node_machine_type" {
    type = string
    default = "e2-medium"
}

variable "node_disk_size" {
    type = number
    default = 50
}

variable "node_number" {
  type    = number
  default = 1
}

########################
#### MYSQL VARIABLES ###
########################

variable "mysql_machine_type" {
    type = string
    default = "e2-medium"
}

variable "mysql_disk_size" {
    type = number
    default = 50
}


########################
#### DB VARIABLES ######
########################

variable "db_machine_type" {
    type = string
    default = "e2-medium"
}

variable "db_disk_size" {
    type = number
    default = 50
}


########################
## PLATFORM VARIABLES ##
########################

variable "platform_machine_type" {
    type = string
    default = "e2-medium"
}

variable "platform_disk_size" {
    type = number
    default = 50
}