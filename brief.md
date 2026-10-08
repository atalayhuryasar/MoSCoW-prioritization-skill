# MoSCoW Prioritization Skill — AI Agent Execution Brief

**Belge Türü:** AI Agent Brief & Yol Haritası
**Proje:** `moscow-prioritization-skill` (Açık Kaynak)
**Hedef Kitle:** Bu brief'i bir AI agent'a (Claude Code, Cursor, Codex, Gemini CLI vb.) verip projeyi baştan sona oluşturmak isteyen geliştirici
**Tahmini Süre:** 2–4 saat (agent ile)
**Versiyon:** 1.0

---

## 1. Bağlam (Context)

Kullanıcı, ürün geliştiren insanlar için MoSCoW metodolojisini bir **AI agent skill'i** haline getirmek istiyor. Bu skill:

- Gereksinimleri Must / Should / Could / Won't olarak kategorize eder
- **60/20/20 kuralını** otomatik denetler
- Karar günlüğü ve kapsam sınırı belgesi üretir
- Açık kaynak olarak yayınlanacak ve birden fazla AI agent platformunda çalışacak

Kullanıcı ayrıca bu projeyi **AI agent kullanarak** inşa etmek istiyor. Yani agent, hem projenin konusu hem de projenin yapıcısı.

---

## 2. Hedefler (Objectives)

| # | Hedef | Başarı Kriteri |
|---|-------|----------------|
| O1 | Açık kaynak depo iskeletini oluştur | GitHub'da public repo, tüm standart dosyalar mevcut |
| O2 | `SKILL.md` dosyasını Agent Skills standardına uygun yaz | Frontmatter doğru, tetikleyiciler tanımlı, prosedür adım adım |
| O3 | 60/20/20 kuralını denetleyen çalışan bir validator yaz | `python scripts/validate_moscow.py examples/input.json` hatasız çalışır |
| O4 | Çoklu platform adaptörlerini oluştur | `.claude/`, `.cursor/`, `.gemini/`, `.agents/` dizinleri hazır |
| O5 | Örnek girdi/çıktı ile skill'i test et | Örnek çıktı, 60/20/20 kuralına uygun |
| O6 | Dokümantasyonu tamamla | README, CONTRIBUTING, CODE_OF_CONDUCT, CHANGELOG mevcut |
| O7 | Lisans ekle | MIT lisansı depo kökünde |

---

## 3. Teslimatlar (Deliverables)

```
moscow-prioritization-skill/
├── README.md                              ✅ O6
├── LICENSE                                ✅ O7
├── CONTRIBUTING.md                        ✅ O6
├── CODE_OF_CONDUCT.md                     ✅ O6
├── CHANGELOG.md                           ✅ O6
├── .gitignore                             ✅ O1
├── install.sh                             ✅ O4
├── skills/
│   └── moscow-prioritization/
│       ├── SKILL.md                       ✅ O2
│       └── references/
│           ├── moscow-method.md
│           └── 60-20-20-rule.md
├── scripts/
│   └── validate_moscow.py                 ✅ O3
├── examples/
│   ├── input.json
│   └── output.md                          ✅ O5
├── adapters/
│   ├── claude-code/README.md              ✅ O4
│   ├── cursor/README.md                   ✅ O4
│   ├── gemini-cli/README.md               ✅ O4
│   ├── codex/README.md                    ✅ O4
│   └── copilot/README.md                  ✅ O4
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 4. AI Agent İçin Yürütme Planı (Execution Plan)

### Faz 0: Hazırlık (5 dk)

**Agent'a talimat:**
```
1. Kullanıcıdan şu bilgileri al:
   - GitHub kullanıcı adı
   - Tercih edilen lisans (varsayılan: MIT)
   - Hedef platformlar (varsayılan: hepsi)
2. Çalışma dizinini doğrula: `pwd`
3. Git kurulu mu kontrol et: `git --version`
4. GitHub CLI kurulu mu kontrol et: `gh --version` (opsiyonel)
```

**Çıktı:** Kullanıcı bilgileri ve ortam doğrulaması.

---

### Faz 1: Depo İskeleti (10 dk)

**Agent'a talimat:**
```
1. `moscow-prioritization-skill/` klasörünü oluştur
2. Aşağıdaki alt dizinleri oluştur:
   - skills/moscow-prioritization/references
   - scripts
   - examples
   - adapters/{claude-code,cursor,gemini-cli,codex,copilot}
   - .github/ISSUE_TEMPLATE
3. `git init` çalıştır
4. `.gitignore` dosyasını oluştur (Python, OS, IDE, build)
```

**Çıktı:** Boş dizin yapısı + git başlangıcı.

---

### Faz 2: `SKILL.md` Yazımı (30 dk)

**Agent'a talimat:**
```
1. `skills/moscow-prioritization/SKILL.md` dosyasını oluştur
2. YAML frontmatter ekle:
   - name: moscow-prioritization
   - description: Tetikleyici ifadeleri içersin ("prioritize", "MoSCoW",
     "MVP scope", "backlog triage", "what to build first")
   - version: 0.1.0
   - license: MIT
   - tags: [product-management, prioritization, mvp, moscow]
3. Gövde bölümleri:
   - Purpose
   - When to use this skill
   - Inputs
   - Procedure (7 adım: validate → collect context → categorize →
     document rationale → enforce 60/20/20 → produce output → decision log)
   - Output format (Markdown tablo örneği)
   - Rules and guardrails
   - Related skills
   - References
4. Dosyayı 500 satırın altında tut
5. Uzun referans materyalini `references/` klasörüne taşı
```

**Kabul kriteri:**
- Frontmatter geçerli YAML
- En az 5 tetikleyici ifade `description` alanında
- 60/20/20 kuralı prosedürde açıkça belirtilmiş
- Örnek çıktı tablosu mevcut

---

### Faz 3: Referans Dokümanları (15 dk)

**Agent'a talimat:**
```
1. `references/moscow-method.md` oluştur:
   - Dört kategori (M/S/C/W) tanımı
   - Her kategori için "test" sorusu
   - 60/20/20 kuralı özeti
   - Yaygın tuzaklar
2. `references/60-20-20-rule.md` oluştur:
   - Tahsis tablosu (M≤60%, S~20%, C~20%, W=0%)
   - "Neden 60%?" açıklaması
   - Uyarı işaretleri
   - Validator kullanım örneği
```

**Kabul kriteri:** Her iki dosya da `SKILL.md` içinden referans verilmiş.

---

### Faz 4: Validator Script'i (30 dk)

**Agent'a talimat:**
```
1. `scripts/validate_moscow.py` oluştur:
   - Python 3.8+ uyumlu, sadece stdlib kullan
   - Girdi: JSON dosyası yolu (argv[1])
   - JSON formatı: {"items": [{"name": str, "category": str, "effort": float}]}
   - Kategoriler: must, should, could, wont
   - Hesapla: her kategorinin toplam eforu ve yüzdesi
   - Kontrol et:
     * Must ≤ 60% → değilse ❌ uyarı
     * Should 15–25% arası → değilse ⚠️ uyarı
     * Could 15–25% arası → değilse ⚠️ uyarı
   - Çıktı: okunabilir konsol raporu
2. `chmod +x scripts/validate_moscow.py`
3. Geçersiz kategori için uyarı ver ama çökme
4. Toplam efor 0 ise bilgi mesajı ver, çık
```

**Kabul kriteri:**
```bash
python scripts/validate_moscow.py examples/input.json
# Çıktı: tüm kategoriler, yüzdeler, ✅/⚠️/❌ işaretleri
```

---

### Faz 5: Örnek Girdi/Çıktı (15 dk)

**Agent'a talimat:**
```
1. `examples/input.json` oluştur:
   - Coffee Shop Mobile App senaryosu
   - En az 13 öğe
   - Dağılım: 4 must, 3 should, 3 could, 3 wont
   - Must toplam eforu ≤ 60% olacak şekilde ayarla
2. `examples/output.md` oluştur:
   - MoSCoW matrisi (tablo)
   - 60/20/20 kontrolü (yüzdelerle)
   - Karar günlüğü (her öğe için gerekçe)
   - Kapsam sınırı (Won't Have listesi)
   - Sonraki adımlar
3. Validator'ı örnek girdiyle çalıştır, çıktıyı doğrula
```

**Kabul kriteri:** `python scripts/validate_moscow.py examples/input.json` çıktısı `output.md` ile tutarlı.

---

### Faz 6: Dokümantasyon (30 dk)

**Agent'a talimat:**
```
1. `README.md` oluştur:
   - Başlık + MIT badge
   - "Why this skill?" bölümü
   - Quick Start (3 adım)
   - Repository structure (ağaç görünümü)
   - Usage (tetikleyici ifadeler)
   - Contributing linki
   - License
2. `CONTRIBUTING.md` oluştur:
   - Fork → branch → commit → PR akışı
   - Validator çalıştırma zorunluluğu
   - Neye katkı beklediğimiz listesi
   - Code of Conduct referansı
3. `CODE_OF_CONDUCT.md` oluştur:
   - Contributor Covenant 2.1 metni
4. `CHANGELOG.md` oluştur:
   - Keep a Changelog formatı
   - [0.1.0] - bugünün tarihi
   - Tüm eklenen özellikleri listele
5. `.github/ISSUE_TEMPLATE/` altına:
   - bug_report.md
   - feature_request.md
6. `.github/PULL_REQUEST_TEMPLATE.md` oluştur
```

**Kabul kriteri:** Tüm dosyalar mevcut ve içerik dolu.

---

### Faz 7: Lisans (5 dk)

**Agent'a talimat:**
```
1. `LICENSE` dosyası oluştur (MIT)
2. Copyright satırı: "Copyright (c) 2026 The MoSCoW Prioritization Skill Contributors"
3. README'de lisans bölümü doğru mu kontrol et
```

---

### Faz 8: Çoklu Platform Adaptörleri (30 dk)

**Agent'a talimat:**
```
1. `install.sh` oluştur:
   - Bash script, set -euo pipefail
   - install_to() fonksiyonu tanımla
   - Şu dizinlere kur:
     * .claude/skills/    → Claude Code
     * .cursor/skills/    → Cursor
     * .gemini/skills/    → Gemini CLI
     * .agents/skills/    → Codex / Copilot
   - LEGACY_CURSOR=1 → .cursorrules oluştur
   - COPILOT_INSTRUCTIONS=1 → .github/copilot-instructions.md oluştur
   - Her kurulum için ✅ mesajı yazdır
2. chmod +x install.sh
3. adapters/ altındaki her platform için README.md yaz:
   - Hedef dizin
   - Kurulum komutu
   - Tetikleyici ifadeler
   - Platforma özel notlar
   - Örnek kullanım
4. install.sh'ı test et (kuru çalıştırma)
```

**Kabul kriteri:** `./install.sh` çalıştırıldığında dört platform dizini oluşur.

---

### Faz 9: Test ve Doğrulama (20 dk)

**Agent'a talimat:**
```
1. Validator'ı çalıştır:
   python scripts/validate_moscow.py examples/input.json
2. Beklenen çıktı:
   - Must Have ≤ 60%
   - Should Have 15–25%
   - Could Have 15–25%
   - Tüm ✅ işaretleri
3. Markdown dosyalarını kontrol et:
   - Tüm linkler çalışıyor mu?
   - Tüm kod blokları dil etiketli mi?
   - Tablolar düzgün render ediliyor mu?
4. SKILL.md frontmatter'ı YAML olarak parse et:
   python -c "import yaml; yaml.safe_load(open('skills/moscow-prioritization/SKILL.md').read().split('---')[1])"
5. install.sh'ı temiz bir dizinde test et
```

**Kabul kriteri:** Tüm testler geçer, hata yok.

---

### Faz 10: GitHub'a Yayınlama (15 dk)

**Agent'a talimat:**
```
1. git add .
2. git commit -m "Initial commit: MoSCoW Prioritization Skill v0.1.0"
3. GitHub CLI varsa:
   gh repo create moscow-prioritization-skill --public --source=. --remote=origin --push
4. GitHub CLI yoksa kullanıcıya şu komutları söyle:
   git remote add origin https://github.com/KULLANICI/moscow-prioritization-skill.git
   git branch -M main
   git push -u origin main
5. GitHub'da repo ayarlarını öner:
   - Description: "AI agent skill for MoSCoW prioritization and MVP scoping"
   - Topics: ai-agents, moscow, prioritization, mvp, product-management, claude-code
   - Discussions: enabled
   - Issues: enabled
```

**Kabul kriteri:** Repo GitHub'da public, tüm dosyalar görünür.

---

## 5. Kısıtlar (Constraints)

| # | Kısıt | Gerekçe |
|---|-------|---------|
| C1 | `SKILL.md` 500 satırın altında olmalı | Token tasarrufu, hızlı yükleme |
| C2 | Validator sadece Python stdlib kullanmalı | Ek kurulum gerektirmemeli |
| C3 | Frontmatter'da sadece standart alanlar | Platformlar arası uyumluluk |
| C4 | Tüm dosyalar UTF-8 ve LF satır sonu | Cross-platform uyumluluk |
| C5 | Lisans MIT olmalı | Geniş benimsenme için |
| C6 | Her kategori ataması gerekçeli olmalı | Öznelliği azaltmak için |
| C7 | Must Have ≤ 60% kuralı ihlal edilirse uyarı | MoSCoW'un özü |

---

## 6. Kabul Kriterleri (Acceptance Criteria)

Proje tamamlanmış sayılır eğer:

- [ ] `python scripts/validate_moscow.py examples/input.json` hatasız çalışıyor
- [ ] Çıktıda Must Have ≤ 60% ve ✅ işareti var
- [ ] `SKILL.md` YAML frontmatter'ı geçerli
- [ ] `SKILL.md` içinde en az 5 tetikleyici ifade var
- [ ] `install.sh` çalıştırıldığında 4 platform dizini oluşuyor
- [ ] README, CONTRIBUTING, CODE_OF_CONDUCT, CHANGELOG, LICENSE mevcut
- [ ] `examples/output.md` 60/20/20 kuralına uygun
- [ ] GitHub'da public repo oluşturuldu
- [ ] Repo topics ve description ayarlandı

---

## 7. Agent İçin Guardrail'ler

**Agent şunları YAPMAMALI:**
- ❌ Kullanıcı onayı olmadan GitHub'a push etmemeli
- ❌ Lisansı değiştirmemeli (MIT sabit)
- ❌ `SKILL.md`'ye platforma özel alanlar eklememeli
- ❌ Validator'a harici bağımlılık eklememeli
- ❌ 60/20/20 kuralını gevşetmemeli
- ❌ Kullanıcının GitHub kullanıcı adını tahmin etmemeli

**Agent şunları YAPMALI:**
- ✅ Her faz sonunda kullanıcıya özet vermeli
- ✅ Hata durumunda durup kullanıcıya sormalı
- ✅ Belirsizlik varsa varsayılanı belirtip onay almalı
- ✅ Tüm dosyaları UTF-8 ve LF ile yazmalı
- ✅ Her adımda doğrulama komutu çalıştırmalı

---

## 8. Agent'a Verilecek Başlangıç Prompt'u

Bu brief'i agent'a verdikten sonra şu prompt'u kullan:

```
Sen kıdemli bir açık kaynak geliştiricisi ve AI agent skill uzmanısın.
Yukarıdaki brief'i baştan sona uygula.

Kurallar:
1. Her fazı sırayla tamamla, atlama.
2. Her faz sonunda bana özet ver ve onay al.
3. Belirsizlik varsa varsayılanı belirt ve sor.
4. GitHub'a push etmeden önce mutlaka onay al.
5. Hata olursa dur ve bana bildir.

Başla: Faz 0 ile başla ve benden gerekli bilgileri iste.
```

---

## 9. Zaman Çizelgesi

| Faz | Süre | Bağımlılık |
|-----|------|------------|
| 0. Hazırlık | 5 dk | — |
| 1. Depo İskeleti | 10 dk | Faz 0 |
| 2. `SKILL.md` | 30 dk | Faz 1 |
| 3. Referanslar | 15 dk | Faz 2 |
| 4. Validator | 30 dk | Faz 1 |
| 5. Örnekler | 15 dk | Faz 4 |
| 6. Dokümantasyon | 30 dk | Faz 2, 4 |
| 7. Lisans | 5 dk | Faz 1 |
| 8. Adaptörler | 30 dk | Faz 2 |
| 9. Test | 20 dk | Faz 3–8 |
| 10. Yayınlama | 15 dk | Faz 9 |
| **Toplam** | **~3.5 saat** | |

---

## 10. Riskler ve Önlemler

| Risk | Olasılık | Etki | Önlem |
|------|----------|------|-------|
| Agent `SKILL.md`'yi çok uzun yazar | Orta | Token israfı | 500 satır kısıtını hatırlat |
| Validator'da edge case hatası | Düşük | Yanlış rapor | Test fazında örnek girdiyle doğrula |
| Platform dizinleri yanlış | Düşük | Skill çalışmaz | `install.sh` test et |
| GitHub push onaysız yapılır | Düşük | İstenmeyen public repo | Guardrail: onay zorunlu |
| Frontmatter YAML hatası | Düşük | Skill yüklenmez | Test fazında parse et |

---

## 11. Sonraki Adımlar (v0.2.0 için)

Proje yayınlandıktan sonra:

- [ ] RICE ve ICE için benzer skill'ler oluştur
- [ ] MoSCoW skill'ini RICE ile karşılaştıran bir benchmark ekle
- [ ] Türkçe, Almanca, İspanyolca çeviriler ekle
- [ ] GitHub Actions ile CI ekle (validator testleri)
- [ ] Skill'i `agentpack` veya `skillpack` ile paketle
- [ ] Hacker News, Reddit r/LocalLLaMA, r/ProductManagement'te duyur
- [ ] İlk "good first issue" konularını aç

---

**Brief Sonu.**

Bu dokümanı bir AI agent'a verip "bu brief'i uygula" dediğinde, agent projeyi baştan sona oluşturabilir. Her faz sonunda senden onay alması ve guardrail'lere uyması için gerekli talimatlar brief içinde yer alıyor.