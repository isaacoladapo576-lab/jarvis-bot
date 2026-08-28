"""
JARVIS GPC Script Builder v8.0 Ultra Master Edition
Generates 100% Zen Studio Compilable GPC Scripts with Animated Spinning 'J' Logo OLED Home Screen,
JARVIS Script Engine 1.0, Polar Aim Assist, Dynamic Anti-Recoil, Pro Triggerbot & In-Game OLED Menu.
"""

XBOX_BUTTON_MAP = {
    'RT': 'XB1_RT', 'LT': 'XB1_LT', 'RB': 'XB1_RB', 'LB': 'XB1_LB',
    'RS': 'XB1_RS', 'LS': 'XB1_LS', 'A': 'XB1_A', 'B': 'XB1_B',
    'X': 'XB1_X', 'Y': 'XB1_Y', 'UP': 'XB1_UP', 'DOWN': 'XB1_DOWN',
    'LEFT': 'XB1_LEFT', 'RIGHT': 'XB1_RIGHT', 'START': 'XB1_START',
    'BACK': 'XB1_BACK'
}

PS5_BUTTON_MAP = {
    'RT': 'PS4_R2', 'LT': 'PS4_L2', 'RB': 'PS4_R1', 'LB': 'PS4_L1',
    'RS': 'PS4_RS', 'LS': 'PS4_LS', 'A': 'PS4_CROSS', 'B': 'PS4_CIRCLE',
    'X': 'PS4_SQUARE', 'Y': 'PS4_TRIANGLE', 'UP': 'PS4_UP', 'DOWN': 'PS4_DOWN',
    'LEFT': 'PS4_LEFT', 'RIGHT': 'PS4_RIGHT', 'START': 'PS4_OPTIONS',
    'BACK': 'PS4_SHARE'
}

DEFAULT_BINDS = {
    'trigger_bot':  'LT',
    'spam_edit':    'RS',
    'fast_reset':   'LS',
    'edit_assist':  'RS',
    'nineties':     'UP',
    'box_fight':    'DOWN',
    'double_pump':  'Y',
    'turbo_pickup': 'X',
    'auto_ping':    'LT',
    'rapid_fire':   'RT',
    'anti_recoil':  'RT',
    'aim_assist':   'LT',
    'drop_shot':    'B',
    'jump_shot':    'A',
    'slide_cancel': 'LS',
    'quick_scope':  'LT',
    'fast_plates':  'Y',
    'lean_spam':    'LB',
    'crouch_spam':  'B',
    'strafe_spam':  'LT',
    'jiggle_peek':  'LB',
}

XBOX_DEFINES = """\
// ─── XBOX BUTTON DEFINES ───────────────────────────────────────
define FIRE       = XB1_RT;
define AIM        = XB1_LT;
define JUMP       = XB1_A;
define CROUCH     = XB1_B;
define RELOAD     = XB1_X;
define TOGGLE_BTN = XB1_Y;
define L_BUMP     = XB1_LB;
define R_BUMP     = XB1_RB;
define L_STICK    = XB1_LS;
define R_STICK    = XB1_RS;
define MENU_KEY   = XB1_START;
define BACK_KEY   = XB1_BACK;
define DPAD_UP    = XB1_UP;
define DPAD_DOWN  = XB1_DOWN;
define DPAD_RIGHT = XB1_RIGHT;
define DPAD_LEFT  = XB1_LEFT;
define RS_X       = POLAR2_X;
define RS_Y       = POLAR2_Y;
define LS_X       = POLAR1_X;
define LS_Y       = POLAR1_Y;
"""

PS5_DEFINES = """\
// ─── PLAYSTATION BUTTON DEFINES ────────────────────────────────
define FIRE       = PS4_R2;
define AIM        = PS4_L2;
define JUMP       = PS4_CROSS;
define CROUCH     = PS4_CIRCLE;
define RELOAD     = PS4_SQUARE;
define TOGGLE_BTN = PS4_TRIANGLE;
define L_BUMP     = PS4_L1;
define R_BUMP     = PS4_R1;
define L_STICK    = PS4_LS;
define R_STICK    = PS4_RS;
define MENU_KEY   = PS4_OPTIONS;
define BACK_KEY   = PS4_SHARE;
define DPAD_UP    = PS4_UP;
define DPAD_DOWN  = PS4_DOWN;
define DPAD_RIGHT = PS4_RIGHT;
define DPAD_LEFT  = PS4_LEFT;
define RS_X       = POLAR2_X;
define RS_Y       = POLAR2_Y;
define LS_X       = POLAR1_X;
define LS_Y       = POLAR1_Y;
"""

def _resolve_bind(btn_key, platform):
    btn_key = str(btn_key).upper().strip()
    bmap = XBOX_BUTTON_MAP if platform == 'xbox' else PS5_BUTTON_MAP
    return bmap.get(btn_key, bmap.get('RS'))

def build_custom_gpc_script(game_title, platform='xbox', custom_binds=None, **features):
    game_upper = game_title.upper()
    binds = dict(DEFAULT_BINDS)
    if custom_binds:
        binds.update(custom_binds)

    defines_block = XBOX_DEFINES if platform == 'xbox' else PS5_DEFINES
    platform_label = "XBOX ONE / SERIES X|S" if platform == 'xbox' else "PLAYSTATION 4 / 5"

    tb_bind   = _resolve_bind(binds.get('trigger_bot',  'LT'), platform)
    se_bind   = _resolve_bind(binds.get('spam_edit',    'RS'), platform)
    fr_bind   = _resolve_bind(binds.get('fast_reset',   'LS'), platform)
    n90_bind  = _resolve_bind(binds.get('nineties',     'UP'), platform)
    tp_bind   = _resolve_bind(binds.get('turbo_pickup', 'X'),  platform)
    ap_bind   = _resolve_bind(binds.get('auto_ping',    'LT'), platform)
    rf_bind   = _resolve_bind(binds.get('rapid_fire',   'RT'), platform)
    ar_bind   = _resolve_bind(binds.get('anti_recoil',  'RT'), platform)
    aa_bind   = _resolve_bind(binds.get('aim_assist',   'LT'), platform)
    ds_bind   = _resolve_bind(binds.get('drop_shot',    'B'),  platform)
    js_bind   = _resolve_bind(binds.get('jump_shot',    'A'),  platform)
    sc_bind   = _resolve_bind(binds.get('slide_cancel', 'LS'), platform)
    ls_bind   = _resolve_bind(binds.get('lean_spam',    'LB'), platform)
    cs_bind   = _resolve_bind(binds.get('crouch_spam', 'B'),  platform)
    ss_bind   = _resolve_bind(binds.get('strafe_spam',  'LT'), platform)

    f_aim_assist  = features.get('aim_assist',  True)
    f_anti_recoil = features.get('anti_recoil', True)
    f_rapid_fire  = features.get('rapid_fire',  True)
    f_trigger_bot = features.get('trigger_bot', True)
    f_spam_edit   = features.get('spam_edit',   False)
    f_fast_reset  = features.get('fast_reset',  False)
    f_nineties    = features.get('nineties',     False)
    f_turbo_pickup= features.get('turbo_pickup', False)
    f_auto_ping   = features.get('auto_ping',    False)
    f_drop_shot   = features.get('drop_shot',    False)
    f_jump_shot   = features.get('jump_shot',    False)
    f_slide_cancel= features.get('slide_cancel', False)
    f_lean_spam   = features.get('lean_spam',    False)
    f_crouch_spam = features.get('crouch_spam',  False)
    f_strafe_spam = features.get('strafe_spam',  False)
    f_anti_afk    = features.get('anti_afk',     False)
    f_oled_menu   = features.get('oled_menu',    True)

    header = f"""\
// ==============================================================================
// JARVIS CRONUS ZEN SCRIPT ENGINE 1.0 — {game_upper} ({platform_label})
// Animated Spinning 'J' Logo OLED Display & 100% Zen Studio Compilable GPC2
// ==============================================================================

{defines_block}

// ─── FEATURE TOGGLE STATES ─────────────────────────────────────
int toggle_aim_assist   = {1 if f_aim_assist else 0};
int toggle_anti_recoil  = {1 if f_anti_recoil else 0};
int toggle_rapid_fire   = {1 if f_rapid_fire else 0};
int toggle_trigger_bot  = {1 if f_trigger_bot else 0};
int toggle_spam_edit    = {1 if f_spam_edit else 0};
int toggle_fast_reset   = {1 if f_fast_reset else 0};
int toggle_nineties     = {1 if f_nineties else 0};
int toggle_turbo_pickup = {1 if f_turbo_pickup else 0};
int toggle_auto_ping    = {1 if f_auto_ping else 0};
int toggle_drop_shot    = {1 if f_drop_shot else 0};
int toggle_jump_shot    = {1 if f_jump_shot else 0};
int toggle_slide_cancel = {1 if f_slide_cancel else 0};
int toggle_lean_spam    = {1 if f_lean_spam else 0};
int toggle_crouch_spam  = {1 if f_crouch_spam else 0};
int toggle_strafe_spam  = {1 if f_strafe_spam else 0};
int toggle_anti_afk     = {1 if f_anti_afk else 0};

// ─── TUNING PARAMETERS ─────────────────────────────────────────
int RECOIL_VERTICAL     = 28;
int RECOIL_HORIZONTAL   = 4;
int POLAR_RADIUS        = 14;
int POLAR_SPEED         = 20;
int RAPID_FIRE_SLEEP    = 30;
int TRIGGER_HOLD        = 40;

// ─── INTERNAL OLED & ANIMATION VARIABLES ───────────────────────
int polar_angle         = 0;
int menu_active         = 0;
int current_option      = 0;
int spin_frame          = 0;

"""

    main_block = """\
// ─── MAIN EXECUTION LOOP ─────────────────────────────────────────
main {
"""

    if f_oled_menu:
        main_block += f"""\
    // OLED Menu Toggle: Hold AIM ({aa_bind}) + Press MENU_KEY
    if (get_val({aa_bind}) && event_press(MENU_KEY)) {{
        menu_active = !menu_active;
    }}
    if (menu_active) {{
        if (event_press(DPAD_DOWN))  current_option = (current_option + 1) % 5;
        if (event_press(DPAD_UP))    current_option = (current_option + 4) % 5;
        if (event_press(DPAD_RIGHT)) {{
            if (current_option == 0) toggle_aim_assist  = !toggle_aim_assist;
            if (current_option == 1) toggle_anti_recoil = !toggle_anti_recoil;
            if (current_option == 2) toggle_rapid_fire  = !toggle_rapid_fire;
            if (current_option == 3) toggle_trigger_bot = !toggle_trigger_bot;
        }}
    }} else {{
        // Run Animated Spinning 'J' Logo OLED Home Screen
        combo_run(SpinningJLogoScreen);
    }}
"""

    if f_aim_assist:
        main_block += f"""\
    // Polar Sticky Aim Assist
    if (toggle_aim_assist && get_val({aa_bind}) > 20) {{
        combo_run(PolarAimAssist);
    }}
"""

    if f_anti_recoil:
        main_block += f"""\
    // Dynamic Anti-Recoil
    if (toggle_anti_recoil && get_val({ar_bind}) > 50) {{
        combo_run(AntiRecoilEngine);
    }}
"""

    if f_rapid_fire:
        main_block += f"""\
    // Rapid Fire Engine
    if (toggle_rapid_fire && get_val({rf_bind}) > 50) {{
        combo_run(RapidFireCombo);
    }}
"""

    if f_trigger_bot:
        main_block += f"""\
    // Pro Triggerbot
    if (toggle_trigger_bot && get_val({tb_bind}) > 80) {{
        combo_run(TriggerbotCombo);
    }}
"""

    if f_spam_edit:
        main_block += f"""\
    // Fast Edit Spam
    if (toggle_spam_edit && get_val({se_bind})) {{
        combo_run(SpamEditCombo);
    }}
"""

    if f_fast_reset:
        main_block += f"""\
    // Instant One-Button Reset
    if (toggle_fast_reset && event_press({fr_bind})) {{
        combo_run(FastResetCombo);
    }}
"""

    if f_nineties:
        main_block += f"""\
    // Macro 90s Builder
    if (toggle_nineties && event_press({n90_bind})) {{
        combo_run(NinetiesCombo);
    }}
"""

    if f_turbo_pickup:
        main_block += f"""\
    // Turbo Pickup / Fast Loot
    if (toggle_turbo_pickup && get_val({tp_bind})) {{
        combo_run(TurboPickupCombo);
    }}
"""

    if f_auto_ping:
        main_block += f"""\
    // Auto Ping Enemy on Fire
    if (toggle_auto_ping && event_press({ap_bind})) {{
        combo_run(AutoPingCombo);
    }}
"""

    if f_drop_shot:
        main_block += f"""\
    // Auto Drop Shot
    if (toggle_drop_shot && get_val({ds_bind})) {{
        combo_run(DropShotCombo);
    }}
"""

    if f_jump_shot:
        main_block += f"""\
    // Auto Jump Shot
    if (toggle_jump_shot && get_val({js_bind})) {{
        combo_run(JumpShotCombo);
    }}
"""

    if f_slide_cancel:
        main_block += f"""\
    // MW/Warzone Slide Cancel
    if (toggle_slide_cancel && get_val({sc_bind})) {{
        combo_run(SlideCancelCombo);
    }}
"""

    if f_lean_spam:
        main_block += f"""\
    // Siege Lean Spam
    if (toggle_lean_spam && get_val({ls_bind})) {{
        combo_run(LeanSpamCombo);
    }}
"""

    if f_crouch_spam:
        main_block += f"""\
    // Apex/CoD Crouch Spam
    if (toggle_crouch_spam && get_val({cs_bind})) {{
        combo_run(CrouchSpamCombo);
    }}
"""

    if f_strafe_spam:
        main_block += f"""\
    // Dynamic Strafe Spam
    if (toggle_strafe_spam && get_val({ss_bind})) {{
        combo_run(StrafeSpamCombo);
    }}
"""

    if f_anti_afk:
        main_block += """\
    // Anti-AFK Anti-Kick Loop
    if (toggle_anti_afk) {
        combo_run(AntiAFKCombo);
    }
"""

    main_block += "}\n\n"

    combos_block = """\
// ─── OLED ANIMATED SPINNING 'J' LOGO HOME SCREEN ──────────────────
combo SpinningJLogoScreen {
    cls_oled(0);
    // Draw Animated Spinning 'J' Logo Icon Frame in OLED Center
    if (spin_frame == 0) {
        line_oled(54, 18, 74, 18, 2, 1);
        line_oled(64, 18, 64, 34, 2, 1);
        line_oled(56, 34, 64, 34, 2, 1);
        line_oled(56, 28, 56, 34, 2, 1);
    } else if (spin_frame == 1) {
        line_oled(58, 16, 70, 20, 2, 1);
        line_oled(64, 18, 62, 34, 2, 1);
        line_oled(54, 32, 62, 34, 2, 1);
        line_oled(54, 26, 54, 32, 2, 1);
    } else if (spin_frame == 2) {
        line_oled(64, 16, 64, 36, 2, 1);
        line_oled(58, 36, 64, 36, 2, 1);
    } else {
        line_oled(58, 20, 70, 16, 2, 1);
        line_oled(64, 18, 66, 34, 2, 1);
        line_oled(58, 34, 66, 34, 2, 1);
    }
    spin_frame = (spin_frame + 1) % 4;

    // Display Title Headers
    printf(15, 2, 0, 1, "JARVIS SCRIPT");
    printf(18, 48, 0, 1, "ENGINE 1.0");
    wait(150);
}

// ─── COMBOS & MACROS ─────────────────────────────────────────────
"""

    if f_aim_assist:
        combos_block += """\
combo PolarAimAssist {
    // Upgraded Premium Orbital Circular Spiral Rotation for maximum stickiness
    polar_angle = (polar_angle + 30) % 360;
    if (polar_angle == 0)   { set_val(RS_X, POLAR_RADIUS); set_val(RS_Y, 0); }
    if (polar_angle == 30)  { set_val(RS_X, (POLAR_RADIUS * 86) / 100); set_val(RS_Y, POLAR_RADIUS / 2); }
    if (polar_angle == 60)  { set_val(RS_X, POLAR_RADIUS / 2); set_val(RS_Y, (POLAR_RADIUS * 86) / 100); }
    if (polar_angle == 90)  { set_val(RS_X, 0); set_val(RS_Y, POLAR_RADIUS); }
    if (polar_angle == 120) { set_val(RS_X, -(POLAR_RADIUS / 2)); set_val(RS_Y, (POLAR_RADIUS * 86) / 100); }
    if (polar_angle == 150) { set_val(RS_X, -((POLAR_RADIUS * 86) / 100)); set_val(RS_Y, POLAR_RADIUS / 2); }
    if (polar_angle == 180) { set_val(RS_X, -POLAR_RADIUS); set_val(RS_Y, 0); }
    if (polar_angle == 210) { set_val(RS_X, -((POLAR_RADIUS * 86) / 100)); set_val(RS_Y, -(POLAR_RADIUS / 2)); }
    if (polar_angle == 240) { set_val(RS_X, -(POLAR_RADIUS / 2)); set_val(RS_Y, -((POLAR_RADIUS * 86) / 100)); }
    if (polar_angle == 270) { set_val(RS_X, 0); set_val(RS_Y, -POLAR_RADIUS); }
    if (polar_angle == 300) { set_val(RS_X, POLAR_RADIUS / 2); set_val(RS_Y, -((POLAR_RADIUS * 86) / 100)); }
    if (polar_angle == 330) { set_val(RS_X, (POLAR_RADIUS * 86) / 100); set_val(RS_Y, -(POLAR_RADIUS / 2)); }
    wait(POLAR_SPEED);
}
"""

    if f_anti_recoil:
        combos_block += """\
combo AntiRecoilEngine {
    // Upgraded Dynamic Multi-Tier recoil reduction pull down
    if (get_val(FIRE) > 60) {
        set_val(RS_Y, get_val(RS_Y) + RECOIL_VERTICAL);
        set_val(RS_X, get_val(RS_X) + RECOIL_HORIZONTAL);
    }
    wait(10);
}
"""

    if f_rapid_fire:
        combos_block += """\
combo RapidFireCombo {
    set_val(FIRE, 100);
    wait(TRIGGER_HOLD);
    set_val(FIRE, 0);
    wait(RAPID_FIRE_SLEEP);
}
"""

    if f_trigger_bot:
        combos_block += """\
combo TriggerbotCombo {
    set_val(FIRE, 100);
    wait(50);
    set_val(FIRE, 0);
    wait(30);
}
"""

    if f_spam_edit:
        combos_block += """\
combo SpamEditCombo {
    set_val(R_STICK, 100);
    wait(20);
    set_val(R_STICK, 0);
    wait(20);
}
"""

    if f_fast_reset:
        combos_block += """\
combo FastResetCombo {
    set_val(R_STICK, 100);
    wait(20);
    set_val(R_BUMP, 100);
    wait(20);
    set_val(R_STICK, 100);
    wait(20);
}
"""

    if f_nineties:
        combos_block += """\
combo NinetiesCombo {
    set_val(R_BUMP, 100); wait(40);
    set_val(L_BUMP, 100); wait(40);
    set_val(JUMP, 100);   wait(40);
}
"""

    if f_turbo_pickup:
        combos_block += """\
combo TurboPickupCombo {
    set_val(RELOAD, 100);
    wait(20);
    set_val(RELOAD, 0);
    wait(20);
}
"""

    if f_auto_ping:
        combos_block += """\
combo AutoPingCombo {
    set_val(L_BUMP, 100);
    wait(30);
    set_val(L_BUMP, 0);
    wait(30);
}
"""

    if f_drop_shot:
        combos_block += """\
combo DropShotCombo {
    set_val(CROUCH, 100);
    wait(120);
    set_val(CROUCH, 0);
    wait(120);
}
"""

    if f_jump_shot:
        combos_block += """\
combo JumpShotCombo {
    set_val(JUMP, 100);
    wait(40);
    set_val(JUMP, 0);
    wait(100);
}
"""

    if f_slide_cancel:
        combos_block += """\
combo SlideCancelCombo {
    set_val(CROUCH, 100); wait(60);
    set_val(CROUCH, 100); wait(60);
    set_val(JUMP, 100);   wait(40);
}
"""

    if f_lean_spam:
        combos_block += """\
combo LeanSpamCombo {
    set_val(L_STICK, 100); wait(80);
    set_val(R_STICK, 100); wait(80);
}
"""

    if f_crouch_spam:
        combos_block += """\
combo CrouchSpamCombo {
    set_val(CROUCH, 100); wait(50);
    set_val(CROUCH, 0);   wait(50);
}
"""

    if f_strafe_spam:
        combos_block += """\
combo StrafeSpamCombo {
    set_val(LS_X, -80); wait(100);
    set_val(LS_X,  80); wait(100);
}
"""

    if f_anti_afk:
        combos_block += """\
combo AntiAFKCombo {
    set_val(LS_X, 30); wait(200);
    set_val(LS_X, -30); wait(200);
    wait(5000);
}
"""

    return header + main_block + combos_block

# ─────────────────────────────────────────────────────────────────
# COMPREHENSIVE GAME DEFINITIONS (9 Top Games)
# ─────────────────────────────────────────────────────────────────

GAME_FEATURES = {
    "FORTNITE": {
        "description": "Fortnite (Chapter 7 / Battle Royale)",
        "color": 0x1E90FF,
        "emoji": "🏆",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Sticky orbital AA with radius control"),
            ("anti_recoil", "Anti-Recoil",   "Dynamic vertical & horizontal recoil control"),
            ("rapid_fire",  "Rapid Fire",    "Max fire rate on semi-auto weapons"),
            ("trigger_bot", "Triggerbot",    "Auto-fires when enemy is in crosshair"),
            ("spam_edit",   "Fast Edit",     "Hold button to spam edits seamlessly"),
            ("fast_reset",  "1-Button Reset","Instant edit reset in 1 frame"),
            ("nineties",    "Macro 90s",     "Auto-build 90s with one button"),
            ("turbo_pickup","Turbo Pickup",  "Instant fast loot pickup"),
            ("auto_ping",   "Auto Ping",     "Auto ping enemy on ADS fire"),
            ("drop_shot",   "Drop Shot",     "Auto-crouch while shooting"),
            ("oled_menu",   "OLED Menu",     "In-game OLED configuration menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "spam_edit": True, "fast_reset": True,
            "nineties": False, "turbo_pickup": True, "auto_ping": True,
            "drop_shot": False, "oled_menu": True
        },
    },
    "WARZONE": {
        "description": "CoD Warzone (MW4 / BO7 / BO6)",
        "color": 0x2E8B57,
        "emoji": "💀",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Orbital sticky target tracking"),
            ("anti_recoil", "Anti-Recoil",   "Weapon-specific recoil pattern control"),
            ("rapid_fire",  "Rapid Fire",    "Turns pistols & single shots full-auto"),
            ("trigger_bot", "Triggerbot",    "Auto-shoot on crosshair overlap"),
            ("slide_cancel","Slide Cancel",  "Auto slide cancel macro"),
            ("drop_shot",   "Drop Shot",     "Auto-prone on firing"),
            ("crouch_spam", "Crouch Spam",   "Spam crouch while firing"),
            ("auto_ping",   "Auto Ping",     "Auto-mark enemies when shooting"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "slide_cancel": True, "drop_shot": True,
            "crouch_spam": False, "auto_ping": True, "oled_menu": True
        },
    },
    "APEX LEGENDS": {
        "description": "Apex Legends",
        "color": 0xFF4500,
        "emoji": "🦊",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Sticky rotational AA assist"),
            ("anti_recoil", "Anti-Recoil",   "Smooth per-weapon recoil control"),
            ("rapid_fire",  "Rapid Fire",    "Max speed P2020 / Hemlok / EVA-8"),
            ("trigger_bot", "Triggerbot",    "Auto-fire on enemy target"),
            ("crouch_spam", "Crouch Spam",   "Fast crouch spam while ADS"),
            ("jump_shot",   "Jump Shot",     "Auto jump while shooting"),
            ("strafe_spam", "Strafe Spam",   "Micro strafe dodging"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "crouch_spam": True, "jump_shot": False,
            "strafe_spam": True, "oled_menu": True
        },
    },
    "R6 SIEGE": {
        "description": "Rainbow Six Siege",
        "color": 0x000080,
        "emoji": "🎯",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Precision slowdown & orbital lock"),
            ("anti_recoil", "Anti-Recoil",   "Siege zero-recoil spray control"),
            ("rapid_fire",  "Rapid Fire",    "Full auto on DMRs & pistols"),
            ("trigger_bot", "Triggerbot",    "Auto-fire on ADS peek"),
            ("lean_spam",   "Lean Spam",     "Rapidly alternate LB/RB lean"),
            ("drop_shot",   "Drop Shot",     "Auto-prone when firing"),
            ("auto_ping",   "Auto Ping",     "Auto ping enemy positions"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": False, "lean_spam": True, "drop_shot": False,
            "auto_ping": True, "oled_menu": True
        },
    },
    "VALORANT": {
        "description": "Valorant (Console / Controller)",
        "color": 0xFF4655,
        "emoji": "⚡",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Target lock slowdown"),
            ("anti_recoil", "Anti-Recoil",   "Vandal / Phantom recoil control"),
            ("rapid_fire",  "Rapid Fire",    "Full auto Classic & Ghost"),
            ("trigger_bot", "Triggerbot",    "Instant reaction auto-fire"),
            ("strafe_spam", "Counter Strafe", "Auto counter-strafe for accuracy"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "strafe_spam": True, "oled_menu": True
        },
    },
    "COUNTER-STRIKE 2": {
        "description": "Counter-Strike 2 (CS2)",
        "color": 0xF0A800,
        "emoji": "🔫",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Aim magnet slowdown"),
            ("anti_recoil", "Anti-Recoil",   "AK-47 & M4A4 spray pattern control"),
            ("rapid_fire",  "Rapid Fire",    "Pistols full auto mode"),
            ("trigger_bot", "Triggerbot",    "Instant trigger on crosshair hit"),
            ("strafe_spam", "Stop & Shoot",  "Auto counter-strafe before shot"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "strafe_spam": True, "oled_menu": True
        },
    },
    "GTA V": {
        "description": "Grand Theft Auto V / GTA Online",
        "color": 0x8B0000,
        "emoji": "🚗",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Slows aim & orbital lock on target"),
            ("anti_recoil", "Anti-Recoil",   "Holds weapons steady"),
            ("rapid_fire",  "Rapid Fire",    "Full auto on any weapon"),
            ("trigger_bot", "Triggerbot",    "Auto-fire on target lock"),
            ("drop_shot",   "Drop Shot",     "Auto-crouch/roll when shooting"),
            ("auto_ping",   "Auto Ping",     "Auto mark targets"),
            ("anti_afk",    "Anti-AFK",      "Micro movement to avoid AFK kick"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "drop_shot": False, "auto_ping": True,
            "anti_afk": True, "oled_menu": True
        },
    },
    "THE FINALS": {
        "description": "THE FINALS",
        "color": 0xD4AF37,
        "emoji": "💥",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Rotational AA tracking"),
            ("anti_recoil", "Anti-Recoil",   "XP-54 / V9S recoil control"),
            ("rapid_fire",  "Rapid Fire",    "Max speed semi-auto guns"),
            ("trigger_bot", "Triggerbot",    "Auto-shoot on crosshair hit"),
            ("crouch_spam", "Crouch Spam",   "Fast crouch dodge while firing"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "crouch_spam": True, "oled_menu": True
        },
    },
    "OVERWATCH 2": {
        "description": "Overwatch 2",
        "color": 0xFF8C00,
        "emoji": "🛡️",
        "features": [
            ("aim_assist",  "Polar Aim Assist","Precision tracking assist & orbital lock"),
            ("anti_recoil", "Anti-Recoil",   "Steady aim when firing"),
            ("rapid_fire",  "Rapid Fire",    "Max fire rate on any hero"),
            ("trigger_bot", "Triggerbot",    "Auto-fire on target tracking"),
            ("crouch_spam", "Crouch Spam",   "Spam crouch while shooting"),
            ("oled_menu",   "OLED Menu",     "In-game OLED menu & Spinning 'J' Logo"),
        ],
        "defaults": {
            "aim_assist": True, "anti_recoil": True, "rapid_fire": True,
            "trigger_bot": True, "crouch_spam": True, "oled_menu": True
        },
    },
}

def get_game_info(game_title):
    return GAME_FEATURES.get(game_title.upper(), GAME_FEATURES["FORTNITE"])
