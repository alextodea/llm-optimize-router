## Requests

### GET
/health → {"status":"ok"}
/metrics → Prometheus histograms/counters (router latency, p95/p99, traffic share, errors).

## POST 

/infer

Request Body
```
{
  "request_id": "optional-uuid",
  "tenant_id": "optional-dev",
  "text": "user prompt",
  "context": {
    "task_type": "chat|summarize|extract|classify|codegen|sql",
    "output_format": "text|json",
    "json_schema_id": "optional-id", 
    "language": "en",
    "context_tokens": 850,         
    "streaming": true,
    "determinism_required": true,  
    "max_latency_ms": 150,         
    "budget_cents_max": 2,         
    "privacy_level": "standard|no_external",
    "domain": "support|legal|code",
    "preferred_models": ["optional-list"],
    "blocked_models": ["optional-list"],
    "lambda_cost": 0.3,            
    "mu_latency": 0.2              
  }
}
```
Output

```
{
  "request_id":"...", "tenant_id":"...", "backend":"arm-name",
  "text":"...", "usage":{"tokens":123,"cost_cents":0.4}, "latency_ms":72,
  "decision_meta":{"utility_hat":0.61,"explore":false}
}
```