#!/usr/bin/env python3
"""Generates the Ink Heist website (EN + TR) into the target folder. Content lives here; layout in style.css."""
import os, sys

OUT = sys.argv[1]
MAIL = "mirzaumt@gmail.com"
UPDATED = {"en": "17 November 2026", "tr": "17 Kasım 2026"}

PAGES = {  # key: (en file, tr file)
    "home": ("index.html", "tr/index.html"),
    "privacy": ("privacy.html", "tr/gizlilik.html"),
    "support": ("support.html", "tr/destek.html"),
    "delete": ("delete-account.html", "tr/hesap-silme.html"),
}
NAV = {"en": [("home", "Home"), ("support", "Support"), ("privacy", "Privacy")],
       "tr": [("home", "Ana sayfa"), ("support", "Destek"), ("privacy", "Gizlilik")]}
FOOT = {"en": [("privacy", "Privacy Policy"), ("support", "Support"), ("delete", "Delete your account")],
        "tr": [("privacy", "Gizlilik Politikası"), ("support", "Destek"), ("delete", "Hesabını sil")]}


def href(lang, key, here_lang):
    path = PAGES[key][0 if lang == "en" else 1]
    if here_lang == "tr":
        return "../" + path if lang == "en" else path[3:]
    return path


def page(lang, key, title, desc, body):
    root = "../" if lang == "tr" else ""
    other = "tr" if lang == "en" else "en"
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{href(lang, k, lang)}"{cur if k == key else ""}>{t}</a>' for k, t in NAV[lang])
    nav += f'<a class="lang" href="{href(other, key, lang)}" hreflang="{other}" lang="{other}">{"Türkçe" if other == "tr" else "English"}</a>'
    foot = "".join(f'<a href="{href(lang, k, lang)}">{t}</a>' for k, t in FOOT[lang])
    name = "Ink Heist" if lang == "en" else "Ink Heist (Çiz &amp; Çal)"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{root}assets/icon-512.png">
<link rel="alternate" hreflang="en" href="{root}{PAGES[key][0]}">
<link rel="alternate" hreflang="tr" href="{root}{PAGES[key][1]}">
<link rel="icon" type="image/png" href="{root}assets/favicon.png">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{href(lang, 'home', lang)}"><img src="{root}assets/icon-512.png" alt="" width="40" height="40">{name}</a>
  <nav class="nav" aria-label="{'Site' if lang == 'en' else 'Site menüsü'}">{nav}</nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
  <span>© 2026 Ink Heist · <a href="mailto:{MAIL}">{MAIL}</a></span>
  <nav aria-label="{'Legal' if lang == 'en' else 'Yasal'}">{foot}</nav>
</div></footer>
</body>
</html>
"""


# ------------------------------------------------------------------ home
def home(lang):
    r = "../" if lang == "tr" else ""
    if lang == "en":
        t = dict(logo="logo-en.png", alt="Ink Heist", tag="Draw roads. Steal gold. Lasso thieves!",
                 lead="A real-time 1v1 drawing battle for iPhone and Android. Your ink is a road for your thieves and a wall for theirs. Matches last about 90 seconds.",
                 soon="Coming soon", vid="Ink Heist gameplay: two players draw ink roads and walls while thieves race for gold.",
                 how="How it plays",
                 f=[("thief_0_a.png", "Draw", "Your ink is a road for your thieves and a wall for your rival's. Plan a route, block theirs."),
                    ("head_1.png", "Lasso", "Circle a rival thief carrying gold with your ink. Lasso! The gold comes back."),
                    ("coin.png", "Steal", "Grab the gold bags that drop in the middle. Most gold when time runs out wins.")],
                 shots="In the game", caps=["Draw a road for your thieves.", "Grab the gold bag first!", "Gold Rush: double gold.", "Win the heist!"], promise_h="Fair by design",
                 promise=["Real money only buys looks. Never power.", "No paid loot boxes. You always see what you get.",
                          "Bots are always labeled BOT. PvP is real players only.", "No free-text chat. Preset emotes and quick messages only.",
                          "The server decides every match result.", "Free to play."],
                 title="Ink Heist: real-time 1v1 drawing battles",
                 desc="Draw roads, steal gold, lasso thieves. A real-time 1v1 drawing game for iPhone and Android.")
    else:
        t = dict(logo="logo-tr.png", alt="Çiz &amp; Çal (Ink Heist)", tag="Yol çiz. Altın çal. Hırsızı kementle!",
                 lead="iPhone ve Android için gerçek zamanlı 1v1 çizim düellosu. Çizdiğin mürekkep kendi hırsızlarına yol, rakibinkilere duvar olur. Maçlar yaklaşık 90 saniye sürer.",
                 soon="Yakında", vid="Ink Heist oynanışı: iki oyuncu mürekkeple yol ve duvar çizerken hırsızlar altın için yarışıyor.",
                 how="Nasıl oynanır",
                 f=[("thief_0_a.png", "Çiz", "Mürekkebin kendi hırsızlarına yol, rakibinkilere duvar. Yolunu planla, onunkini kes."),
                    ("head_1.png", "Kementle", "Altın taşıyan rakip hırsızın etrafını çiz. Kement! Altın geri gelir."),
                    ("coin.png", "Çal", "Ortaya düşen altın çuvallarını kap. Süre bitince en çok altını olan kazanır.")],
                 shots="Oyundan kareler", caps=["Hırsızlarına yol çiz.", "Altın çuvalını ilk sen kap!", "Kement: hırsızı çiz, altını geri al.", "Ana menü: PvP veya botlarla antrenman."], promise_h="Adil olsun diye tasarlandı",
                 promise=["Gerçek parayla sadece görünüm alınır, asla güç.", "Ücretli sürpriz kutu yok. Ne alacağını her zaman görürsün.",
                          "Botlar her zaman BOT yazar. PvP sadece gerçek oyuncular.", "Serbest yazışma yok. Sadece hazır emojiler ve mesajlar.",
                          "Her maçın sonucuna sunucu karar verir.", "Ücretsiz oyna."],
                 title="Ink Heist (Çiz & Çal): gerçek zamanlı 1v1 çizim düellosu",
                 desc="Yol çiz, altın çal, hırsızı kementle. iPhone ve Android için gerçek zamanlı 1v1 çizim oyunu.")
    feats = "".join(f'<div class="card feature"><img src="{r}assets/{i}" alt="" width="72" height="72"><h3>{h}</h3><p>{p}</p></div>' for i, h, p in t["f"])
    shots = "".join(f'<figure><img src="{r}assets/{lang}-shot-{n}.jpg" alt="{c}" width="600" height="1304" loading="lazy"><figcaption>{c}</figcaption></figure>' for n, c in enumerate(t["caps"], 1))
    prom = "".join(f"<li>{x}</li>" for x in t["promise"])
    body = f"""
<section class="hero">
  <div>
    <h1><img src="{r}assets/{t['logo']}" alt="{t['alt']}" width="900" height="570"></h1>
    <p class="tagline">{t['tag']}</p>
    <p class="lead">{t['lead']}</p>
    <div class="badges">
      <span class="badge"><span><small>App Store</small>{t['soon']}</span></span>
      <span class="badge"><span><small>Google Play</small>{t['soon']}</span></span>
    </div>
  </div>
  <div class="phone">
    <video src="{r}assets/teaser.mp4" poster="{r}assets/teaser-poster.jpg" autoplay muted loop playsinline aria-label="{t['vid']}"></video>
    <img class="poster" src="{r}assets/teaser-poster.jpg" alt="{t['vid']}">
  </div>
</section>
<section><h2>{t['how']}</h2><div class="grid3">{feats}</div></section>
<section><h2>{t['shots']}</h2><div class="shots">{shots}</div></section>
<section><div class="card"><h2>{t['promise_h']}</h2><ul class="promise">{prom}</ul></div></section>
"""
    return t["title"], t["desc"], body


# ------------------------------------------------------------------ privacy
def privacy(lang):
    if lang == "en":
        rows = [
            ("Game account ID", "A random ID the app creates on your device, and the account ID our server assigns.", "To save your progress."),
            ("Apple or Google sign-in (optional)", "An account identifier from Apple or Google. We do not ask for your name or email address.", "To keep your progress on every device."),
            ("Age group", "You enter your birth year on the device. Only the age group (under 13, 13–17 or 18+) is sent. The year never leaves your device.", "To give each age group the right features and limits."),
            ("Nickname and looks", "A nickname built from our word lists (no free text), your avatar and cosmetics.", "To show your opponent who they are playing."),
            ("Progress and stats", "Level, XP, coins, gems, unlocks, match results and a hidden skill rating.", "Progression, rewards and fair matchmaking."),
            ("Match inputs", "The lines you draw and the powers you use during a match.", "Our server replays the match to decide the result and stop cheating."),
            ("Purchases", "Product, transaction ID and receipt from Apple or Google. Payment details stay with Apple or Google; we never see your card.", "To deliver what you bought, prevent fraud, handle refunds and apply spending limits for minors."),
            ("Friends and quick messages (13+ only)", "Your friend code, friend list, friend requests and blocks, recent opponents, online/last-seen time, and the preset quick messages you send to friends (we keep the last 50 per conversation, with times). There is no free text.", "So you can add friends, see who is online, send preset messages and play friendly matches."),
            ("Gifts", "Gifts our team sends you (coins, gems or items, with a short note) and whether you claimed them.", "To deliver gifts and compensation into your inbox."),
            ("Notifications (only if you allow them)", "A push token, your time-zone offset, language and notification settings.", "Reminders and match calls at sensible times. Never sent to players under 13."),
            ("Technical data", "IP address, device and system type, and server logs.", "To connect you, keep the service secure and fix problems."),
        ]
        table = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
        body = f"""
<article class="card doc">
<h1>Privacy Policy</h1>
<p class="meta">Last updated: {UPDATED['en']}</p>
<p>Ink Heist (called “Çiz &amp; Çal” in Turkish) is a mobile game made by an independent developer. This policy explains what data the game uses and why. Questions: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<div class="callout"><strong>In short:</strong> no ads, no tracking or analytics tools, no data selling, no free-text chat, and we never ask for your name or email address.</div>

<h2>What we collect and why</h2>
<div class="table-scroll"><table>
<thead><tr><th>Data</th><th>What it is</th><th>Why</th></tr></thead>
<tbody>{table}</tbody></table></div>
<p>Legal bases (EU/UK GDPR and Turkish KVKK): running the game you asked for (contract); security, anti-cheat and fixing problems (legitimate interests); notifications (your consent, which you can withdraw in Settings or in your phone's settings); keeping purchase records (legal obligation).</p>

<h2>What we do not do</h2>
<ul>
<li>We do not show ads or use advertising IDs.</li>
<li>We do not track you across other apps or websites.</li>
<li>We do not sell or rent personal data.</li>
<li>We do not offer free-text chat. Players can only send preset emotes and preset quick messages.</li>
</ul>

<h2>Who we share data with</h2>
<ul>
<li><strong>Apple and Google</strong>, for sign-in, in-app purchases and push notifications. Their own privacy policies apply.</li>
<li><strong>Our hosting provider</strong>, which runs our servers and processes data only on our behalf.</li>
<li><strong>Authorities</strong>, only when the law requires it.</li>
</ul>
<p>Your opponent sees your nickname, avatar, looks and level during a match. Your friends also see whether you are online or when you were last seen. Anyone with your friend code can send you a friend request; you can decline or block them at any time.</p>

<h2>Children</h2>
<p>We ask for a birth year with a neutral screen. Players under 13 get a limited account: no push notifications, no friends or messages, they cannot be found by friend code, and purchases are turned off unless a parent unlocks them. Purchases are off by default for everyone under 18 and have a monthly limit. A parent can ask us to delete a child's data at any time by email.</p>

<h2>How long we keep data</h2>
<p>We keep your data while your account exists. When you delete your account, we delete your account, profile, progress, wallet, notification registration, friend list, friend code, messages and gifts. We keep purchase transaction records for as long as needed to prevent fraud, handle refunds and meet tax and legal duties. Server logs are kept for a limited time. If you play as a guest and delete the app, the ID on your device is gone and that progress can no longer be recovered.</p>
<p>How to delete your account: <a href="{href('en', 'delete', 'en')}">Delete your account</a>.</p>

<h2>Your rights</h2>
<p>You can ask to access, correct, delete or export your data, or object to how we use it. Email <a href="mailto:{MAIL}">{MAIL}</a> and we will reply within 30 days. You can also complain to your local data protection authority.</p>

<h2>Where data is processed</h2>
<p>Our servers and service providers may be in a country other than yours. When data leaves your region, we use the safeguards the law requires.</p>

<h2>Security</h2>
<p>We use reasonable technical and organisational measures to protect your data, such as restricted access and keeping secret keys out of our code.</p>

<h2>Changes</h2>
<p>If we change this policy, we will update the date at the top and, for important changes, tell you in the game.</p>
</article>"""
        return "Privacy Policy: Ink Heist", "What data Ink Heist uses, why, and how to delete it.", body
    rows = [
        ("Oyun hesabı kimliği", "Uygulamanın cihazında oluşturduğu rastgele bir kimlik ve sunucumuzun verdiği hesap kimliği.", "İlerlemeni kaydetmek."),
        ("Apple veya Google ile giriş (isteğe bağlı)", "Apple ya da Google'dan gelen bir hesap kimliği. Adını veya e-posta adresini istemiyoruz.", "İlerlemeni her cihazda korumak."),
        ("Yaş grubu", "Doğum yılını cihazda girersin. Sadece yaş grubu (13 altı, 13–17, 18+) gönderilir. Yıl cihazından çıkmaz.", "Her yaş grubuna uygun özellikleri ve sınırları sunmak."),
        ("Takma ad ve görünüm", "Kelime listelerimizden oluşan takma ad (serbest metin yok), avatar ve kozmetikler.", "Rakibine kiminle oynadığını göstermek."),
        ("İlerleme ve istatistikler", "Seviye, XP, coin, elmas, açılan içerikler, maç sonuçları ve gizli beceri puanı.", "İlerleme, ödüller ve adil eşleştirme."),
        ("Maç girdileri", "Maç sırasında çizdiğin çizgiler ve kullandığın güçler.", "Sunucumuz maçı yeniden oynatıp sonucu belirler ve hileyi önler."),
        ("Satın almalar", "Apple veya Google'dan ürün, işlem numarası ve makbuz. Ödeme bilgilerin Apple veya Google'da kalır; kartını asla görmeyiz.", "Satın aldığını teslim etmek, dolandırıcılığı önlemek, iadeleri yürütmek ve reşit olmayanlar için harcama sınırı uygulamak."),
        ("Arkadaşlar ve hazır mesajlar (sadece 13+)", "Arkadaş kodun, arkadaş listen, arkadaşlık istekleri ve engellediklerin, son rakiplerin, çevrimiçi/son görülme zamanın ve arkadaşlarına gönderdiğin hazır mesajlar (her sohbette son 50 mesaj, zamanıyla). Serbest metin yoktur.", "Arkadaş ekleyebilmen, kimin çevrimiçi olduğunu görebilmen, hazır mesaj gönderebilmen ve dostluk maçı oynayabilmen için."),
        ("Hediyeler", "Ekibimizin gönderdiği hediyeler (coin, elmas veya eşya ve kısa bir not) ve alıp almadığın.", "Hediye ve telafileri gelen kutuna ulaştırmak."),
        ("Bildirimler (sadece izin verirsen)", "Bildirim anahtarı, saat dilimi farkı, dil ve bildirim ayarların.", "Uygun saatlerde hatırlatma ve maç çağrısı. 13 yaş altına asla gönderilmez."),
        ("Teknik veriler", "IP adresi, cihaz ve sistem türü, sunucu kayıtları.", "Bağlantını kurmak, hizmeti güvende tutmak ve sorunları gidermek."),
    ]
    table = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    body = f"""
<article class="card doc">
<h1>Gizlilik Politikası</h1>
<p class="meta">Son güncelleme: {UPDATED['tr']}</p>
<p>Ink Heist (Türkçede “Çiz &amp; Çal”) bağımsız bir geliştiricinin yaptığı bir mobil oyundur. Bu metin oyunun hangi verileri neden kullandığını açıklar. Sorular için: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<div class="callout"><strong>Kısaca:</strong> reklam yok, takip veya analitik aracı yok, veri satışı yok, serbest yazışma yok; adını ya da e-posta adresini asla istemiyoruz.</div>

<h2>Neleri, neden topluyoruz</h2>
<div class="table-scroll"><table>
<thead><tr><th>Veri</th><th>Nedir</th><th>Neden</th></tr></thead>
<tbody>{table}</tbody></table></div>
<p>Hukuki dayanaklar (KVKK ve AB/Birleşik Krallık GDPR): istediğin oyunu sunmak (sözleşme); güvenlik, hile önleme ve sorun giderme (meşru menfaat); bildirimler (açık rızan; Ayarlar'dan veya telefonunun ayarlarından geri alabilirsin); satın alma kayıtlarını saklamak (yasal yükümlülük).</p>

<h2>Yapmadıklarımız</h2>
<ul>
<li>Reklam göstermiyor, reklam kimliği kullanmıyoruz.</li>
<li>Seni başka uygulama veya sitelerde takip etmiyoruz.</li>
<li>Kişisel verileri satmıyor veya kiralamıyoruz.</li>
<li>Serbest yazışma yok. Oyuncular sadece hazır emojiler ve hazır mesajlar gönderebilir.</li>
</ul>

<h2>Verileri kimlerle paylaşıyoruz</h2>
<ul>
<li><strong>Apple ve Google</strong>: giriş, uygulama içi satın alma ve bildirimler için. Onların gizlilik politikaları geçerlidir.</li>
<li><strong>Barındırma sağlayıcımız</strong>: sunucularımızı çalıştırır ve verileri sadece bizim adımıza işler.</li>
<li><strong>Resmi makamlar</strong>: sadece yasa gerektirdiğinde.</li>
</ul>
<p>Rakibin maç sırasında takma adını, avatarını, görünümünü ve seviyeni görür. Arkadaşların ayrıca çevrimiçi olup olmadığını veya en son ne zaman görüldüğünü görür. Arkadaş kodunu bilen herkes sana arkadaşlık isteği gönderebilir; istediğin zaman reddedebilir veya engelleyebilirsin.</p>

<h2>Çocuklar</h2>
<p>Doğum yılını tarafsız bir ekranla soruyoruz. 13 yaş altındaki oyuncular sınırlı bir hesap alır: bildirim yok, arkadaş ve mesaj yok, arkadaş koduyla bulunamazlar ve bir ebeveyn açmadıkça satın alma kapalıdır. 18 yaş altındaki herkes için satın alma varsayılan olarak kapalıdır ve aylık sınırı vardır. Ebeveynler çocuklarının verilerinin silinmesini istedikleri zaman e-postayla isteyebilir.</p>

<h2>Verileri ne kadar saklıyoruz</h2>
<p>Hesabın var olduğu sürece verilerini saklarız. Hesabını sildiğinde hesabını, profilini, ilerlemeni, cüzdanını, bildirim kaydını, arkadaş listeni, arkadaş kodunu, mesajlarını ve hediyelerini sileriz. Satın alma işlem kayıtlarını dolandırıcılığı önlemek, iadeleri yürütmek ve vergi/yasal yükümlülükleri yerine getirmek için gerektiği kadar saklarız. Sunucu kayıtları sınırlı bir süre tutulur. Misafir olarak oynayıp uygulamayı silersen cihazındaki kimlik de silinir ve o ilerleme artık geri getirilemez.</p>
<p>Hesabını nasıl silersin: <a href="{href('tr', 'delete', 'tr')}">Hesabını sil</a>.</p>

<h2>Hakların</h2>
<p>Verilerine erişmeyi, düzeltilmesini, silinmesini veya dışa aktarılmasını isteyebilir, işlenmesine itiraz edebilirsin. <a href="mailto:{MAIL}">{MAIL}</a> adresine yaz; 30 gün içinde yanıt veririz. Kişisel Verileri Koruma Kurumu'na veya bulunduğun ülkedeki veri koruma otoritesine şikâyette de bulunabilirsin.</p>

<h2>Veriler nerede işleniyor</h2>
<p>Sunucularımız ve hizmet sağlayıcılarımız senin ülkenden farklı bir ülkede olabilir. Veriler yurt dışına aktarıldığında yasanın gerektirdiği güvenceleri uygularız.</p>

<h2>Güvenlik</h2>
<p>Verilerini korumak için erişimi kısıtlamak ve gizli anahtarları kodumuzun dışında tutmak gibi makul teknik ve idari önlemler alıyoruz.</p>

<h2>Değişiklikler</h2>
<p>Bu politikayı değiştirirsek üstteki tarihi güncelleriz; önemli değişiklikleri oyun içinde de duyururuz.</p>
</article>"""
    return "Gizlilik Politikası: Ink Heist (Çiz & Çal)", "Ink Heist hangi verileri neden kullanıyor ve nasıl silinir.", body


# ------------------------------------------------------------------ support
def support(lang):
    if lang == "en":
        faq = [
            ("How do I keep my progress on a new phone?", "Open <strong>Profile → Account</strong> and sign in with Apple or Google. Then sign in with the same account on your new phone. Guest progress is saved on one device only."),
            ("Am I playing against bots?", "PvP matches are real players only. Bots appear only in <strong>Practice vs Bots</strong>, and they are always labeled BOT."),
            ("A purchase didn't arrive or I want a refund.", "Close and reopen the game first; purchases are delivered when the store confirms them. Refunds are handled by the store: on iPhone at <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>, on Android in Google Play under <em>Payments &amp; subscriptions → Budget &amp; history</em>. If it still looks wrong, email us."),
            ("How do I turn off notifications?", "In the game: <strong>Settings → Reminders</strong> or <strong>Match calls</strong>. You can also turn them off in your phone's settings."),
            ("Can I chat with other players?", "No. To keep the game safe, there is no free-text chat. You can send preset emotes in a match (and turn rival emotes off in Settings), and players 13 and older can send preset quick messages like “GG!” or “Wanna play?” to friends."),
            ("How do I add a friend?", "Open Friends in the main menu. Share your 6-letter friend code, type a friend's code, or add someone from Recent opponents. You can remove or block anyone at any time. Friends are available from age 13."),
            ("How do I delete my account?", f"See <a href=\"{href('en', 'delete', 'en')}\">Delete your account</a>."),
        ]
        items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
        body = f"""
<article class="card doc">
<h1>Support</h1>
<p class="meta">We read every message.</p>
<p>Email us at</p>
<p class="mail"><a href="mailto:{MAIL}?subject=Ink%20Heist%20support">{MAIL}</a></p>
<p>It helps if you include your nickname with its #tag (in <strong>Profile</strong>), your phone model and what happened. Please don't send passwords or payment details.</p>
<h2>Common questions</h2>
{items}
</article>"""
        return "Support: Ink Heist", "Get help with Ink Heist: contact, purchases, progress and account deletion.", body
    faq = [
        ("İlerlememi yeni telefona nasıl taşırım?", "<strong>Profil → Hesap</strong> bölümünden Apple veya Google ile giriş yap. Yeni telefonda aynı hesapla giriş yap. Misafir ilerlemesi sadece tek cihazda saklanır."),
        ("Botlara karşı mı oynuyorum?", "PvP maçları sadece gerçek oyuncularla oynanır. Botlar sadece <strong>Botlarla antrenman</strong> modunda çıkar ve her zaman BOT yazar."),
        ("Satın aldığım gelmedi veya iade istiyorum.", "Önce oyunu kapatıp yeniden aç; satın almalar mağaza onayladığında teslim edilir. İadeleri mağaza yapar: iPhone'da <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>, Android'de Google Play'de <em>Ödemeler ve abonelikler → Bütçe ve geçmiş</em>. Hâlâ bir sorun varsa bize yaz."),
        ("Bildirimleri nasıl kapatırım?", "Oyunda: <strong>Ayarlar → Hatırlatmalar</strong> veya <strong>Maç çağrıları</strong>. Telefonunun ayarlarından da kapatabilirsin."),
        ("Diğer oyuncularla yazışabilir miyim?", "Hayır. Oyunu güvenli tutmak için serbest yazışma yok. Maçta hazır emojiler gönderebilir (rakip emojilerini Ayarlar'dan kapatabilirsin), 13 yaş ve üstü oyuncular arkadaşlarına “GG!” veya “Maç atalım mı?” gibi hazır mesajlar gönderebilir."),
        ("Nasıl arkadaş eklerim?", "Ana menüde Arkadaşlar'ı aç. 6 harfli arkadaş kodunu paylaş, arkadaşının kodunu yaz ya da Son rakipler listesinden ekle. İstediğin kişiyi istediğin zaman çıkarabilir veya engelleyebilirsin. Arkadaşlar 13 yaşından itibaren açıktır."),
        ("Hesabımı nasıl silerim?", f"<a href=\"{href('tr', 'delete', 'tr')}\">Hesabını sil</a> sayfasına bak."),
    ]
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f"""
<article class="card doc">
<h1>Destek</h1>
<p class="meta">Her mesajı okuyoruz.</p>
<p>Bize e-posta gönder:</p>
<p class="mail"><a href="mailto:{MAIL}?subject=Ink%20Heist%20destek">{MAIL}</a></p>
<p>Takma adını #etiketiyle birlikte (<strong>Profil</strong>'de yazar), telefon modelini ve ne olduğunu yazarsan daha hızlı yardımcı olabiliriz. Lütfen şifre veya ödeme bilgisi gönderme.</p>
<h2>Sık sorulanlar</h2>
{items}
</article>"""
    return "Destek: Ink Heist (Çiz & Çal)", "Ink Heist için yardım: iletişim, satın almalar, ilerleme ve hesap silme.", body


# ------------------------------------------------------------------ delete account
def delete(lang):
    if lang == "en":
        body = f"""
<article class="card doc">
<h1>Delete your account</h1>
<p class="meta">Ink Heist (Çiz &amp; Çal)</p>
<h2>In the game</h2>
<ol class="steps">
<li>Open <strong>Profile</strong> from the main menu.</li>
<li>Tap <strong>Account</strong>.</li>
<li>Tap <strong>Delete account</strong>, then tap again to confirm.</li>
</ol>
<p>Your account is deleted right away. This cannot be undone.</p>
<h2>Without the app</h2>
<p>Email <a href="mailto:{MAIL}?subject=Ink%20Heist%20account%20deletion">{MAIL}</a> with the subject “Account deletion”. Include your nickname with its #tag and, if you used it, whether you signed in with Apple or Google. We may ask a question to confirm the account is yours. We delete it within 30 days and confirm by email.</p>
<h2>What is deleted</h2>
<ul>
<li>Your account, nickname, profile and avatar</li>
<li>Progress, stats, unlocks, cosmetics, coins and gems</li>
<li>Your notification registration</li>
<li>Your friend list, friend code, quick messages and gifts</li>
</ul>
<h2>What we keep</h2>
<p>Purchase transaction records (product, date, store transaction ID), for as long as needed to prevent fraud, handle refunds and meet tax and legal duties. Server logs are kept for a limited time. Gems and items in a deleted account cannot be restored or refunded by us.</p>
<p>More detail: <a href="{href('en', 'privacy', 'en')}">Privacy Policy</a>.</p>
</article>"""
        return "Delete your account: Ink Heist", "How to delete your Ink Heist account and data, in the app or by email.", body
    body = f"""
<article class="card doc">
<h1>Hesabını sil</h1>
<p class="meta">Ink Heist (Çiz &amp; Çal)</p>
<h2>Oyunun içinden</h2>
<ol class="steps">
<li>Ana menüden <strong>Profil</strong>'i aç.</li>
<li><strong>Hesap</strong>'a dokun.</li>
<li><strong>Hesabı sil</strong>'e dokun, onaylamak için tekrar dokun.</li>
</ol>
<p>Hesabın hemen silinir. Bu işlem geri alınamaz.</p>
<h2>Uygulama olmadan</h2>
<p><a href="mailto:{MAIL}?subject=Ink%20Heist%20hesap%20silme">{MAIL}</a> adresine “Hesap silme” konulu bir e-posta gönder. Takma adını #etiketiyle birlikte ve kullandıysan Apple ya da Google ile giriş yapıp yapmadığını yaz. Hesabın sana ait olduğunu doğrulamak için bir soru sorabiliriz. Hesabı 30 gün içinde siler, e-postayla haber veririz.</p>
<h2>Neler silinir</h2>
<ul>
<li>Hesabın, takma adın, profilin ve avatarın</li>
<li>İlerlemen, istatistiklerin, açtığın içerikler, kozmetikler, coin ve elmasların</li>
<li>Bildirim kaydın</li>
<li>Arkadaş listen, arkadaş kodun, hazır mesajların ve hediyelerin</li>
</ul>
<h2>Neleri saklarız</h2>
<p>Satın alma işlem kayıtları (ürün, tarih, mağaza işlem numarası): dolandırıcılığı önlemek, iadeleri yürütmek ve vergi/yasal yükümlülükler için gerektiği kadar. Sunucu kayıtları sınırlı bir süre tutulur. Silinen hesaptaki elmas ve eşyaları geri getiremeyiz veya iade edemeyiz.</p>
<p>Ayrıntılar: <a href="{href('tr', 'privacy', 'tr')}">Gizlilik Politikası</a>.</p>
</article>"""
    return "Hesabını sil: Ink Heist (Çiz & Çal)", "Ink Heist hesabını ve verilerini oyundan veya e-postayla nasıl silersin.", body


GEN = {"home": home, "privacy": privacy, "support": support, "delete": delete}
for key, (en, tr) in PAGES.items():
    for lang, path in (("en", en), ("tr", tr)):
        title, desc, body = GEN[key](lang)
        full = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(page(lang, key, title, desc, body))
        print("wrote", path)
