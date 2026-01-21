---
theme: default
title: "Module 2: Tokenization"
description: "Understanding tokenization in NLP systems"
author: ""
keywords: nlp,tokenization,bpe,wordpiece
---

# Tokenization

Module 2

---

## What is Tokenization?

Tokenization is the process of breaking text into smaller units called **tokens**.

```
"Hello, world!" → ["Hello", ",", "world", "!"]
```

---

## Types of Tokenization

### Word-level
Split on whitespace and punctuation

### Subword-level
- **BPE** (Byte Pair Encoding)
- **WordPiece**
- **SentencePiece**

### Character-level
Each character is a token

---

## Byte Pair Encoding (BPE)

1. Start with character vocabulary
2. Find most frequent pair
3. Merge into new token
4. Repeat until vocabulary size reached

```
"lowest" → ["low", "est"]
"lower"  → ["low", "er"]
```

---

## Why Subword Tokenization?

- Handles out-of-vocabulary words
- Balances vocabulary size and sequence length
- Captures morphological patterns

---

## Summary

- Tokenization converts text to model input
- Subword methods are most common today
- Choice affects model performance
