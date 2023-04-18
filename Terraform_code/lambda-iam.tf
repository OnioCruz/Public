data "aws_iam_policy_document" "lambda_assum_role_policy"{
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy" "lambda_policy" {
  name = "lambda_policy"
  role = aws_iam_role.lambda_role.id

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = "${file("iam/lambda-policy.json")}"
}
resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"

  assume_role_policy = "${file("iam/lambda-assume-policy.json")}"}