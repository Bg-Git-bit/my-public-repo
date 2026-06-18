# Output values from Terraform

output "glue_job_name" {
  description = "Name of the created Glue job"
  value       = aws_glue_job.data_transformation.name
}

output "glue_job_arn" {
  description = "ARN of the created Glue job"
  value       = aws_glue_job.data_transformation.arn
}

output "cloudwatch_log_group" {
  description = "CloudWatch log group for Glue job"
  value       = aws_cloudwatch_log_group.glue_logs.name
}

output "script_location" {
  description = "S3 location of Glue script"
  value       = "s3://${var.s3_output_bucket}/scripts/aws_glue_Script_1.py"
}
