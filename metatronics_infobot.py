"""
METATRONICS Info Bot
====================
Setup:
  pip install python-telegram-bot==21.3
  python metatronics_infobot.py
"""

import asyncio
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ContextTypes
)

TOKEN = "8364700775:AAGttF0k8P3hQsuo8tRLoFHudXcTsWZyvPA"

logging.basicConfig(level=logging.INFO)

def nav(*buttons):
    rows = []
    row = []
    for i, (label, cmd) in enumerate(buttons):
        row.append(InlineKeyboardButton(label, callback_data=cmd))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return InlineKeyboardMarkup(rows)

def main_menu():
    return nav(
        ("📊 Algorithm",    "algorithm"),
        ("🚀 Get Started",  "getstarted"),
        ("💰 Profit",       "profit"),
        ("🏦 Withdrawal",   "withdrawal"),
        ("⚠️ Risks",        "risks"),
        ("🤝 Partners",     "partners"),
        ("⚡ Fast Start",   "faststart"),
        ("🏆 Ranks",        "ranks"),
        ("🌐 Ecosystem",    "ecosystem"),
        ("🗺 Roadmap",      "roadmap"),
        ("🪙 Token",        "token"),
        ("🛟 Support",      "support"),
        ("📞 Contacts",     "contacts"),
        ("❓ FAQ",          "faq"),
    )

def back_home():
    return nav(("← Main Menu", "home"))

def back_and(label, cmd):
    return nav(("← Main Menu", "home"), (label, cmd))

SCREENS = {}

SCREENS["home"] = (
    "🤖 *METATRONICS Info Bot*\n\n"
    "Your reference guide to the platform\\.\n"
    "Choose a topic below — or visit [metatronics\\.me](https://metatronics.me/en)\\.",
    main_menu()
)

SCREENS["about"] = (
    "📌 *About METATRONICS*\n\n"
    "METATRONICS is an AI\\-powered algorithmic trading platform built inside Telegram\\.\n\n"
    "No manual trading\\. No guesswork\\. The algorithm runs 24/7, closes positions every day at 00:00 UTC, and distributes profit automatically\\.\n\n"
    "📍 Registered entity: VIENNA HOLDING LIMITED — 7/F MW Tower, Hong Kong\n\n"
    "Key numbers:\n"
    "• 214\\.5% — total return since launch\n"
    "• 58,000\\+ active users\n"
    "• 4 strategies running simultaneously\n"
    "• Deposit from $5\n"
    "• 15\\+ payment providers\n\n"
    "[Open Platform](https://t.me/MetatronicsBot/METATRONICS?startapp=ref_FS2E96AHAB47)",
    back_home()
)

SCREENS["algorithm"] = (
    "⚙️ *How the Algorithm Works*\n\n"
    "METATRONICS runs 4 strategies in parallel — all drawing from one shared pool:\n\n"
    "🔵 *Hedge* — neutralizes market direction risk\\. Positions offset each other\\.\n"
    "📈 *Trend* — follows confirmed momentum\\. Enters after signal confirmation\\.\n"
    "⚡ *Arbitrage* — exploits price gaps across exchanges\\. 89% historical win rate\\.\n"
    "🔁 *Scalp* — high\\-frequency micro\\-trades\\. Hundreds of entries per session\\.\n\n"
    "The system analyzes 47,000\\+ market scenarios per day\\. Execution speed: under 50ms\\. Maximum daily drawdown: 5% hard limit\\.\n\n"
    "Every session closes at *00:00 UTC*\\. Profit distributes automatically\\.",
    back_and("🚀 Get Started", "getstarted")
)

SCREENS["getstarted"] = (
    "🚀 *How to Get Started*\n\n"
    "Three steps\\. Under 60 seconds\\.\n\n"
    "*Step 1 — Open the platform*\n"
    "Tap the button below\\. Log in with your Telegram account\\. No KYC, no documents\\.\n\n"
    "*Step 2 — Fund your account*\n"
    "Deposit from $5 via card, crypto \\(7 networks\\), or Telegram Stars\\.\n"
    "Supported networks: TRC20, BEP20, ERC20, TON, Polygon, Arbitrum, Solana\\.\n\n"
    "*Step 3 — Allocate to strategies*\n"
    "Move funds from General Balance → Trading Balance\\. Choose your strategies\\. The algorithm starts immediately\\.\n\n"
    "Profit lands in your Profit Balance every day at 00:00 UTC\\.\n\n"
    "[Open METATRONICS ↗](https://t.me/MetatronicsBot/METATRONICS?startapp=ref_FS2E96AHAB47)",
    back_and("💰 Profit", "profit")
)

SCREENS["profit"] = (
    "💰 *How Profit Works*\n\n"
    "Your daily profit depends on three variables:\n\n"
    "1️⃣ *Your share of the pool* — calculated proportionally based on your Trading Balance relative to the total pool\\.\n\n"
    "2️⃣ *Session result* — the actual trading outcome of that day\\. Results vary\\. No fixed rate\\.\n\n"
    "3️⃣ *Time in pool* — profit accrues from the moment funds enter Trading Balance\\.\n\n"
    "Every day at *00:00 UTC*, the algorithm closes positions\\. Your share of the session result is credited to your *Profit Balance*\\.\n\n"
    "*Example:* $1,000 in pool at 1\\.6% session return → ~$16 credited to Profit Balance\\.\n\n"
    "From Profit Balance you can: withdraw, compound \\(move back to Trading\\), or leave it\\.\n\n"
    "Compounding = exponential growth\\. Withdrawing = liquidity\\. Both are always available\\.",
    back_and("🏦 Withdrawal", "withdrawal")
)

SCREENS["withdrawal"] = (
    "🏦 *Withdrawal Options*\n\n"
    "No lock\\-up\\. Withdraw anytime\\. Minimum: $20\\.\n\n"
    "Choose your withdrawal speed:\n\n"
    "⚡ *Instant* — fee: 10%\n"
    "🔄 *2\\-day cycle* — fee: 5%\n"
    "🔄 *4\\-day cycle* — fee: 3%\n"
    "🔄 *6\\-day cycle* — fee: 2%\n"
    "✅ *10\\-day cycle* — fee: 0%\n\n"
    "Wait longer = pay less\\. Instant withdrawal always available\\.\n\n"
    "Withdrawals go to the same method you deposited\\. Processing is automatic after the cycle ends\\.",
    back_home()
)

SCREENS["risks"] = (
    "⚠️ *Risks — The Honest Version*\n\n"
    "METATRONICS runs real algorithmic trading\\. Real trading carries real risk\\.\n\n"
    "What we guarantee:\n"
    "✅ Maximum daily drawdown: 5% hard limit \\(system stops if hit\\)\n"
    "✅ Full transparency of daily results\n"
    "✅ No lock\\-up — withdraw anytime\n"
    "✅ Registered legal entity\n\n"
    "What we do NOT guarantee:\n"
    "❌ Fixed daily or monthly returns\n"
    "❌ Profit on every session\n"
    "❌ Protection from market conditions\n\n"
    "Past performance \\(214\\.5% total return\\) does not guarantee future results\\.\n\n"
    "Invest only what you can afford to keep in the market\\.",
    back_home()
)

SCREENS["partners"] = (
    "🤝 *Partner Program*\n\n"
    "Earn from your team's daily trading profit — not from their deposits\\.\n\n"
    "*10 referral levels:*\n"
    "Level 1 → 10%\n"
    "Level 2 → 5%\n"
    "Level 3 → 3%\n"
    "Level 4 → 2%\n"
    "Level 5 → 1\\.5%\n"
    "Levels 6–10 → 0\\.5% each\n\n"
    "*Total: up to 24% of your network's daily profit\\.*\n\n"
    "How to unlock levels:\n"
    "Each $1,000 of active team turnover unlocks the next level\\.\n"
    "Or: make a $10,000 personal deposit — all 10 levels activate immediately\\.\n\n"
    "Commissions accrue daily\\. Paid to your General Balance automatically\\.",
    back_and("⚡ Fast Start", "faststart")
)

SCREENS["faststart"] = (
    "⚡ *Fast Start Bonus*\n\n"
    "Get \\+20% to your personal trading income for the first month\\.\n\n"
    "*Conditions:*\n"
    "1\\. Make your first deposit\n"
    "2\\. Within 7 days — invite 3 partners\n"
    "3\\. Each partner deposits an amount ≥ your deposit\n\n"
    "*Result:* \\+20% added to your trading return for 30 days\\.\n\n"
    "Example: if the algorithm returns 1\\.6% on a session, you get 1\\.92% instead\\.\n\n"
    "The bonus activates automatically once all 3 conditions are met\\.",
    back_and("🏆 Ranks", "ranks")
)

SCREENS["ranks"] = (
    "🏆 *Rank System*\n\n"
    "5 ranks based on total team trading turnover\\.\n"
    "Rewards are real and paid 30 days after milestone is reached\\.\n\n"
    "🥇 *Rank 1* — $50,000 team turnover → Company event trips\n"
    "📱 *Rank 2* — $100,000 → iPhone 17 Pro Max\n"
    "⌚ *Rank 3* — $500,000 → Rolex watch\n"
    "🚗 *Rank 4* — $3,000,000 → Tesla car\n"
    "🏙 *Rank 5* — $10,000,000 → Dubai apartment \\+ Ambassador status\n\n"
    "*Rules:*\n"
    "• No more than 50% of the required turnover can come from one team branch\n"
    "• Rewards are paid once, 30 days after milestone confirmation\n\n"
    "[View full Rank System ↗](https://drive.google.com/file/d/1e8C2g8-39yDB2I3Xc6vFZ5T7ErL_BCTE/view?usp=drive_link)",
    back_home()
)

SCREENS["ecosystem"] = (
    "🌐 *METATRONICS Ecosystem*\n\n"
    "One account\\. Everything in one place\\.\n\n"
    "✅ *Trading Platform* — live now\n"
    "4 AI strategies, daily profit, instant withdrawal\n\n"
    "📚 *MetaAcademy* — Phase IV\n"
    "50\\+ lessons on trading, crypto, and risk management\n\n"
    "📡 *Signal Bot* — Phase IV\n"
    "Algorithmic trade signals with built\\-in risk filters\n\n"
    "🔒 *MetaVPN* — Phase IV\n"
    "Secure connection for traders\\. Always\\-on protection\n\n"
    "🪙 *METATRONICS Token* — Phase V\n"
    "In development\\. No launch date yet\\. Will be announced on\\-chain\\.\n\n"
    "[View Roadmap ↗](https://drive.google.com/file/d/1_cZPkWgkSGgi46zKNX6u9KWnMuJ-jN6-/view)",
    back_and("🗺 Roadmap", "roadmap")
)

SCREENS["roadmap"] = (
    "🗺 *Roadmap*\n\n"
    "✅ *Phase I — Foundation* \\(complete\\)\n"
    "Platform launch, 4 strategies, 58,000\\+ users, card payments, Info Bot\n\n"
    "🔄 *Phase II — Scale* \\(in progress\\)\n"
    "Target: 100,000 users\\. Istanbul office\\. Global conference\\. Transparency upgrades\\.\n\n"
    "⏳ *Phase III — Infrastructure*\n"
    "Advanced analytics, expanded payment rails, institutional integrations\n\n"
    "⏳ *Phase IV — Ecosystem*\n"
    "MetaAcademy, Signal Bot, MetaVPN — all launching under one account\n\n"
    "⏳ *Phase V — Token*\n"
    "METATRONICS token launch\\. On\\-chain integration\\. Tokenomics TBD\\.\n\n"
    "⏳ *Phase VI — Global*\n"
    "Regulated markets entry, institutional fund layer\n\n"
    "[Full Roadmap PDF ↗](https://drive.google.com/file/d/1_cZPkWgkSGgi46zKNX6u9KWnMuJ-jN6-/view)",
    back_home()
)

SCREENS["token"] = (
    "🪙 *METATRONICS Token*\n\n"
    "The token does not exist yet — by design\\.\n\n"
    "We chose not to launch a token at the start\\. Reasons:\n\n"
    "• Token value must be backed by real platform activity\n"
    "• We're building the product first, the token second\n"
    "• A premature token launch creates incentives that don't align with user profit\n\n"
    "Current status: *Phase V — planned for 2026–2027*\n\n"
    "When the token launches:\n"
    "• Announced officially in the Telegram channel\n"
    "• On\\-chain verification from day one\n"
    "• No presale to insiders, no hidden allocation\n\n"
    "Follow [@metatronics](https://t.me/metatronics) for updates\\.",
    back_home()
)

SCREENS["support"] = (
    "🛟 *Support*\n\n"
    "Official support channels only:\n\n"
    "📧 Email: support@metatronics\\.me\n"
    "🤖 Bot: @metatronics\\_info\\_bot \\(this bot\\)\n"
    "📢 Channel: @metatronics\n\n"
    "⚠️ *Security warning:*\n"
    "METATRONICS staff will never message you first\\.\n"
    "Never share your seed phrase, private key, or password\\.\n"
    "Verify all links — the only official domain is metatronics\\.me\n\n"
    "For account issues, email support with your Telegram username and a description of the problem\\.",
    back_and("📞 Contacts", "contacts")
)

SCREENS["contacts"] = (
    "📞 *Official Contacts*\n\n"
    "🌐 Website: [metatronics\\.me](https://metatronics.me/en)\n"
    "📱 Platform: [Open Mini App](https://t.me/MetatronicsBot/METATRONICS?startapp=ref_FS2E96AHAB47)\n"
    "📢 Channel: [@metatronics](https://t.me/metatronics)\n"
    "🤖 Info Bot: [@metatronics\\_info\\_bot](https://t.me/metatronics_info_bot)\n"
    "🐦 X \\(Twitter\\): [@metatronics\\_](https://x.com/metatronics_)\n"
    "📝 Medium: [medium\\.com/@metatronics\\.me](https://medium.com/@metatronics.me)\n"
    "📧 Support: support@metatronics\\.me\n\n"
    "📍 Legal entity: VIENNA HOLDING LIMITED\n"
    "7/F MW Tower, 111 Bonham Strand, Sheung Wan, Hong Kong",
    back_home()
)

SCREENS["faq"] = (
    "❓ *FAQ*\n\n"
    "*Is there a minimum deposit?*\n"
    "Yes — $5\\. No maximum\\.\n\n"
    "*Do I need KYC?*\n"
    "No\\. Telegram login only\\.\n\n"
    "*When is profit paid?*\n"
    "Every day at 00:00 UTC\\. Automatically to your Profit Balance\\.\n\n"
    "*Can I withdraw anytime?*\n"
    "Yes\\. Minimum $20\\. Instant withdrawal available at 10% fee\\.\n\n"
    "*Is the return fixed?*\n"
    "No\\. It depends on actual trading results\\. No guarantees\\.\n\n"
    "*What's the max daily loss?*\n"
    "5% hard stop\\. The system stops trading if this limit is hit\\.\n\n"
    "*How do referral commissions work?*\n"
    "You earn a percentage of your team's daily profit — not deposits\\. Up to 24% across 10 levels\\.\n\n"
    "*Where is the company registered?*\n"
    "VIENNA HOLDING LIMITED, Hong Kong\\.\n\n"
    "*Is there a token?*\n"
    "Not yet\\. Planned for Phase V \\(2026–2027\\)\\.",
    back_home()
)

async def cmd_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cmd = update.message.text.lstrip("/").split("@")[0].lower()
    if cmd == "start":
        cmd = "home"
    screen = SCREENS.get(cmd, SCREENS["home"])
    text, keyboard = screen
    await update.message.reply_text(text, parse_mode="MarkdownV2",
                                    reply_markup=keyboard,
                                    disable_web_page_preview=True)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    cmd = query.data.lower()
    screen = SCREENS.get(cmd, SCREENS["home"])
    text, keyboard = screen
    await query.edit_message_text(text, parse_mode="MarkdownV2",
                                  reply_markup=keyboard,
                                  disable_web_page_preview=True)

def main():
    app = Application.builder().token(TOKEN).build()
    for cmd in list(SCREENS.keys()) + ["start", "about"]:
        app.add_handler(CommandHandler(cmd, cmd_handler))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
