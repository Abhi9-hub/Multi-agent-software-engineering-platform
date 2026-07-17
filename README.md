# Forge2 Multi-Agent AI System

Hermes Agent (Brain)
OpenClaw (Coding Agent)
Slack Communication Layer
PostgreSQL Memory
GitHub CI/CD


Current Flow and also adding a verifier loop to make it more automated

Task -> Gen Code -> 
Execute Code -> Verifier 
                        │
                        ▼
        --------------- |
        |               Failed -> Send Error Back -> OpenClaw Retry
        Success -> Memory -> Slack