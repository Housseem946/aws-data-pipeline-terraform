resource "aws_s3_bucket" "data_bucket" {
  bucket = "data-pipeline-bucket-${random_id.bucket_suffix.hex}"
  force_destroy = true
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# Le random_id permet d’avoir un bucket unique (car le nom doit l’être globalement).

