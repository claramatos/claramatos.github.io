Title: Papers
Slug: papers
Date: 2026-03-01
Modified: 2026-03-01

# Models

## Health LLMs

### Google Models

- MedGemma
    - [Jul 2025] MedGemma Technical Report | [paper](https://arxiv.org/abs/2507.05201) | [blog](https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/) | [code](https://github.com/google-health/medgemma) | [models](https://huggingface.co/collections/google/medgemma-release)
- Med-Gemini
    - [May 2024] Capabilities of Gemini Models in Medicine | [paper](https://arxiv.org/abs/2404.18416) | [video](https://www.youtube.com/watch?v=f7uxqDXXMGY)
    - [May 2024] Advancing Multimodal Medical Capabilities of Gemini | [paper](https://arxiv.org/abs/2405.03162)
- Med-PaLM | [blog](https://sites.research.google/gr/med-palm/)
    - [Jul 2023] Towards Generalist Biomedical AI | [paper](https://arxiv.org/abs/2307.14334)
    - [May 2023] Towards Expert-Level Medical Question Answering with Large Language Models | [paper](https://arxiv.org/abs/2305.09617)
    - [Dec 2022] Large language models encode clinical knowledge | [paper](https://arxiv.org/abs/2212.13138) | [video](https://www.youtube.com/watch?v=saWEFDRuNJc)

### LLaMA-based

- [Aug 2024] Med42-v2: A Suite of Clinical LLMs | [paper](https://arxiv.org/abs/2408.06142)
- [Feb 2024] Me LLaMA: Foundation Large Language Models for Medical Applications | [paper](https://arxiv.org/abs/2402.12749)
- [Nov 2023] Meditron-70B: Scaling Medical Pretraining for Large Language Models | [paper](https://arxiv.org/abs/2311.16079) | [code](https://github.com/epfLLM/meditron)
- [Oct 2023] AlpaCare: Instruction-tuned Large Language Models for Medical Application | [paper](https://arxiv.org/abs/2310.14558) | [code](https://github.com/XZhang97666/AlpaCare/tree/master)
- [Apr 2023] PMC-LLaMA: Towards Building Open-source Language Models for Medicine | [paper](https://arxiv.org/abs/2304.14454)

### Open-Source

- [Sep 2025] Baichuan-M2: Scaling Medical Capability with Large Verifier System | [paper](https://arxiv.org/abs/2509.02208) | [mode](https://huggingface.co/collections/baichuan-inc/baichuan-m2)
- [Jul 2024] BioMistral: A Collection of Open-Source Pretrained Large Language Models for Medical Domains | [paper](https://arxiv.org/abs/2402.10373)
- [Aug 2023] Clinical Camel - An open-source expert-level medical language model with dialogue-based knowledge encoding | [paper](https://arxiv.org/abs/2305.12031)
- [Oct 2022] BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining | [paper](https://arxiv.org/abs/2210.10341) | [code](https://github.com/microsoft/BioGPT)
- OpenBioLLM-70B - Open-source medical LLM series (7B-70B parameters) | [model](https://huggingface.co/aaditya/Llama3-OpenBioLLM-70B)

### Wearable & Sensor Models

- [Sep 2025] SensorLM: Learning the Language of Wearable Sensors | [paper](https://arxiv.org/abs/2506.09108)
- [Oct 2024] Scaling Wearable Foundation Models | [paper](https://arxiv.org/abs/2410.13638)

## General LLMs in Health

- [Feb 2026] ChatGPT Health performance in a structured test of triage recommendations | [paper](https://www.nature.com/articles/s41591-026-04297-7#Abs1)
- [Nov 2023] Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine | [paper](https://arxiv.org/abs/2311.16452)

# Evaluation

## Verifiable

- MultiMedQA | [paper](https://arxiv.org/abs/2212.13138) | [data](https://huggingface.co/collections/openlifescienceai/multimedqa)
    - MedQA | [paper](https://arxiv.org/abs/2009.13081) | [data](https://github.com/jind11/MedQA)
    - PubMedQA | [paper](https://arxiv.org/abs/1909.06146) | [data](https://github.com/pubmedqa/pubmedqa)
    - MedMCQA | [paper](https://arxiv.org/abs/2203.14371) | [data](https://medmcqa.github.io)
    - MMLU | [paper](https://arxiv.org/abs/2009.03300) | [code](https://github.com/ollmer/mmlu)
        - Clinical Knowledge | College Medicine | College Biology | Professional Medicine | Anatomy | Medical Genetics
- MMLU Pro | [paper](https://arxiv.org/abs/2406.01574) | [code](https://github.com/TIGER-AI-Lab/MMLU-Pro) | [data](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)
    - Health | Biology | Psychology
- MedNLI | [paper](https://arxiv.org/abs/1808.06752) | [data](https://physionet.org/content/mednli/1.0.0/)
- GeneTuring | [paper](https://www.biorxiv.org/content/10.1101/2023.03.11.532238v1) | [data](https://github.com/ncbi/GeneGPT)
- MedExpQA | [paper](https://arxiv.org/abs/2406.06331)
- MedCaseReasoning | [paper](https://arxiv.org/abs/2505.11733) | [code](https://github.com/kevinwu23/Stanford-MedCaseReasoning)

## Open Ended
- [May 2025] HealthBench: Evaluating Large Language Models Towards Improved Human Health | [paper](https://arxiv.org/abs/2505.08775) | [code](https://github.com/openai/simple-evals) | [data](https://huggingface.co/datasets/openai/healthbench)
- [Jun 2025] MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science | [paper](https://arxiv.org/abs/2506.04405) | [code](https://github.com/wshi83/MedAgentGym) | [docs](https://wshi83.github.io/MedAgentGym-Page/)
- [Jan 2025] MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents | [paper](https://arxiv.org/abs/2501.14654) | [code](https://github.com/stanfordmlgroup/MedAgentBench)

## Safety, Bias & Equity

- [Dec 2025] First, do NOHARM: towards clinically safe large language models | [paper](https://arxiv.org/abs/2512.01241)
- [Oct 2025] MedScore: Factuality Evaluation of Free-Form Medical Answers | [paper](https://arxiv.org/abs/2505.18452v1) | [code](https://github.com/Heyuan9/MedScore)
- [Feb 2025] MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models | [paper](https://arxiv.org/abs/2502.14302) | [code](https://github.com/MedHallu/MedHallu) | [data](https://huggingface.co/datasets/UTAustin-AIHealth/MedHallu) 
- [Mar 2024] A Toolbox for Surfacing Health Equity Harms and Biases in Large Language Models | [paper](https://arxiv.org/abs/2403.12025)
- [Dec 2024] MEDEC: A Benchmark for Medical Error Detection and Correction in Clinical Notes | [paper](https://arxiv.org/abs/2412.19260) | [code](https://github.com/abachaa/MEDEC)
- [Oct 2024] MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models | [paper](https://arxiv.org/abs/2403.03744v5)
- [Oct 2023] Med-HALT: Medical Domain Hallucination Test for Large Language Models | [paper](https://arxiv.org/abs/2307.15343)

## Frameworks & Suites
- [Oct 2025] A Principle-based Framework for the Development and Evaluation of Large Language Models for Health and Wellness | [paper](https://arxiv.org/abs/2512.08936)
- [May 2025] MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks | [paper](https://arxiv.org/abs/2505.23802) | [code](https://github.com/stanford-crfm/helm) | [docs](https://crfm-helm.readthedocs.io/en/latest/medhelm/) | [leaderboard](https://crfm.stanford.edu/helm/medhelm/latest/)

# Applications

## Diagnostic Reasoning

- Copilot Health (Microsoft)
    - [Jun 2025] Sequential Diagnosis with Language Models | [paper](https://arxiv.org/abs/2506.22405)
- AMIE (Google)
    - [Jul 2025] Towards physician-centered oversight of conversational diagnostic AI | [paper](https://arxiv.org/abs/2507.15743)
    - [May 2025] Advancing Conversational Diagnostic AI with Multimodal Reasoning | [paper](https://arxiv.org/abs/2505.04653)
    - [Mar 2025] Towards Conversational AI for Disease Management | [paper](https://arxiv.org/abs/2503.06074)
    - [Jan 2024] Towards Conversational Diagnostic AI | [paper](https://arxiv.org/abs/2401.05654) | [video](https://www.youtube.com/watch?v=KKasKOQAo1k&t=1470s) | [blog](https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/)
    - [Dec 2023] Towards Accurate Differential Diagnosis with Large Language Models | [paper](https://arxiv.org/abs/2312.00164)
    - Specialty Applications:
        - [Oct 2025] Complementary Human-AI Clinical Reasoning in Ophthalmology | [paper](https://arxiv.org/abs/2510.22414)
        - [Nov 2024] Exploring Large Language Models for Specialist-level Oncology Care | [paper](https://arxiv.org/abs/2411.03395)
        - [Oct 2024] Towards Democratization of Subspeciality Medical Expertise | [paper](https://arxiv.org/abs/2410.03741)
- CoDoc:
    - [Jul 2023] Enhancing the reliability and accuracy of AI-enabled diagnosis via complementarity-driven deferral to clinicians | [paper](https://www.nature.com/articles/s41591-023-02437-x) | [code](https://github.com/google-deepmind/codoc)  

## Personal Health & Wearables

- Fitbit (Google)
    - [Sep 2025] Transforming Wearable Data into Personal Health Insights using Large Language Model Agents | [paper](https://arxiv.org/abs/2406.06464)
    - [Aug 2025] The Anatomy of a Personal Health Agent | [paper](https://arxiv.org/abs/2508.20148)
    - [Jun 2024] Transforming Wearable Data into Personal Health Insights using Large Language Model Agents | [paper](https://arxiv.org/abs/2406.06464) | [blog](https://research.google/blog/advancing-personal-health-and-wellness-insights-with-ai/)
    - [Jun 2024] Towards a Personal Health Large Language Model | [paper](https://arxiv.org/abs/2406.06474) | [blog](https://research.google/blog/advancing-personal-health-and-wellness-insights-with-ai/)

# Other
- [Jan 2026] State of Clinical AI Report 2026 | [report](https://arise-ai.org/report)
- [Dec 2024] Generative AI in Medicine | [paper](https://arxiv.org/abs/2412.10337v1)