from binance.um_futures import UMFutures
import time
import datetime
import json
import telebot
import psutil                                       ### для логов контроля оперативной памяти   -eg-
import gc
from typing import List, Dict                       ### для типизации функций                   -eg-


# Константы и параметры
EMOJI_LEVELS = ["😟", "😧😧", "😱😱😱"]          # визуальные метки уровней убытка
HEADERS = ["Счёт", "Нереал.убыток", "Баланс", "Доступ.маржа", "Откр.позиций"]  # заголовки ежечасной таблицы 
WIDTHS = [12, 17, 12, 16, 10]                       # ширины колонок ежечасной таблицы 
PERIOD = 0.25                                       # периодичность проверок в минутах (0.25 == 15 сек.)
LOSS_THRESHOLDS = [5, 15, 50]                       # уровни тревоги по ед.убытку по монете в долларах
# LOSS_THRESHOLDS = [0.1, 0.2, 0.3]                 # отладка, тестирование                     -eg-

min_minutes = -1                                    # минимальное время в минутах (не используется, фильтровать спам)
min_position = 0                                    # минимальная сумма позиции (не используется, фильтровать спам)

# Telegram параметры                                # 🔒 ключи изменены
TG_BOT_TOKEN = "7656400000:AAE9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"   ### t.me/XX_drawer_bot   (ЕГ)
# ALARM_TG = "-10023XXXXXXXX"
# ERROR_TG = '-10023XXXXXXXX'     ### t.me/XX_err   -eg-
ERROR_TG = "-10023XXXXXXXX"       ### Монитор счетов https://t.me/c/23046XXXXX/6
ACCOUNT_TG = "-10023XXXXXXXX"     ### https://t.me/+LltLXXXXXXXXXXXX  https://t.me/c/23046XXXXX/5
# ALARM_TG = "-10023XXXXXXXX"     ### https://t.me/+LltLXXXXXXXXXXXX для отладки всё шлю в группу XX -eg-
# LOGS_TG =  '-10023XXXXXXXX'     ### t.me/XX_logs  -eg-
ALARM_TG = "-10023XXXXXXXX"       ### https://t.me/c/23046XXXXX/5  https://t.me/+LltLXXXXXXXXXXXX

bot = telebot.TeleBot(TG_BOT_TOKEN)

client_0 = UMFutures()                                                      ### только для сбора данных, без торговли -eg-
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 400
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client400 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 402
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client402 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key =  "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"      # 399
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client399 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    API_KEY = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  #401
                                                                                                                                                                                                                                    API_SECRET = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client401 = UMFutures(API_KEY, API_SECRET)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1231
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1231 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1230
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1230 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1035
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1035 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 403
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client403 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1036
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1036 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1037
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1037 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1038
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1038 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1039
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1039 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1040
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1040 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1041
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1041 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1042
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1042 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1043
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1043 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1044
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1044 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1229
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1229 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1232
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1232 = UMFutures(key, secret)
if True:
                                                                                                                                                                                                                                    key = "JzDnyDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"       # 1233
                                                                                                                                                                                                                                    secret = "NWppc6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client1233 = UMFutures(key, secret)                 # создаём клиенты по всем отслеживаемым счетам

# кортеж всех клиентов
client_tpl = (
    client399, client400, client401, client402, client403,
    client1035, client1036, client1037, client1038, client1039,
    client1040, client1041, client1042, client1043, client1044,
    client1229, client1230, client1231, client1232, client1233
)
# список всех номеров счетов                       ### ЗДЕСЬ УКАЖИТЕ СВОИ НОМЕРА/МЕТКИ СЧЕТОВ ###  -eg-
account_ids = ["399", "400", "401", "402", "403",
               "1035", "1036", "1037", "1038", "1039",
               "1040", "1041", "1042", "1043", "1044",
               "1229", "1230", "1231", "1232", "1233"]

already_sent = {aid: {} for aid in account_ids}     # словарь для хранения позиций уже отправленных сообщений
last_report_hour = -1                               # час последней отправки таблицы
disconnected_counter = 0                            # счётчик дисконнектов

def load_state() -> List:
    """
    Загружает состояние из файла 'time_last_check.txt'

    Повторяет попытку чтения до 10 раз с увеличивающейся задержкой между ними
    Если не удалось загрузить — возвращает значения по умолчанию

    Returns:
        List: [время последней проверки, время последнего отчёта, флаг проверки в этот час, день месяца]
    """
    for delay in range(10):
        try:
            with open('/projects/Alarm_bot/time_last_check.txt', 'r') as f:
                return json.loads(f.read())
        except:
            print("delay =", delay, flush=True)
            time.sleep(0.5 + 0.5 * delay)

    # Значения по умолчанию: текущее время, текущее - 15 часов, флаг проверки, текущий день
    return [time.time(), time.time() - 15 * 60 * 60, 0, datetime.datetime.now().day]


def save_state(time_last_check: float, time_last_drawn: float, hour_check_1h_vj: int, check_day_vj: int) -> None:
    """
    Сохраняет текущее состояние в файл 'time_last_check.txt'

    Args:
        time_last_check (float): Время последней проверки
        time_last_drawn (float): Время последнего отчёта
        hour_check_1h_vj (int): Флаг проверки в этот час
        check_day_vj (int): День месяца последней проверки
    """
    try:
        with open('/projects/Alarm_bot/time_last_check.txt', 'w') as f:
            f.write(json.dumps([time_last_check, time_last_drawn, hour_check_1h_vj, check_day_vj]))
    except Exception as e:
        bot.send_message(ERROR_TG, f'!!! Alarm_bot: time_last_check save fail !!!\n{e}')


def load_already_sent() -> Dict[str, Dict[str, int]]:
    """
    Загружает словарь уже отправленных тикеров по счетам из файла 'already_sent.txt'.

    Обновляет устаревший формат (список) в словарь при необходимости.

    Returns:
        Dict[str, Dict[str, int]]: словарь {account_id: {symbol: отметка отправки}}
    """
    try:
        with open('/projects/Alarm_bot/already_sent.txt', 'r') as f:
            raw = json.loads(f.read())

            # меняет старый формат (список) на словарь
            for k, v in raw.items():
                if isinstance(v, list):
                    raw[k] = {symb: 0 for symb in v}

            return raw
    except:
        # Если не удалось — пустой словарь
        return {aid: {} for aid in account_ids}


def save_already_sent(already_sent: Dict[str, Dict[str, int]]) -> None:
    """
    Сохраняет словарь уже отправленных сообщений в файл 'already_sent.txt'

    Args:
        already_sent (Dict[str, Dict[str, int]]): Структура уже отправленных сообщений
    """
    try:
        with open('/projects/Alarm_bot/already_sent.txt', 'w') as f:
            f.write(json.dumps(already_sent))
    except Exception as e:
        bot.send_message(ERROR_TG, f'!!! Alarm_bot: already_sent save fail !!!\n{e}')


def get_formatted_time(timestamp: float) -> str:
    """
    Преобразует временную метку в строку читаемого формата

    Args:
        timestamp (float): Временная метка в миллисекундах

    Returns:
        str: Строка формата "%Y-%m-%d %H:%M:%S"
    """
    dt_object = datetime.datetime.fromtimestamp(timestamp / 1000.0)
    return dt_object.strftime("%Y-%m-%d %H:%M:%S")


def send_hourly_report(accounts_data: List[Dict], time_last_drawn: float) -> float:
    """
    Отправляет отчёт по всем счетам в Telegram раз в час в первые 5 минут

    Производится также замер использования памяти в чат с логами ошибок

    Args:
        accounts_data (List[Dict]): Состояние всех счетов 
        time_last_drawn (float): Время последней отправки отчёта

    Returns:
        float: Новое значение времени последнего отчёта
    """
    now = time.gmtime()
    current_time = time.time()
    current_minute = now.tm_min

    # # === ОТЛАДКА: каждые 10 минут ===
    # if current_minute % 10 != 0:
    #     return time_last_drawn  # ничего не шлём

    # # если отчёт уже отправлялся в эту же минуту — пропускаем
    # if current_time - time_last_drawn < 60:
    #     return time_last_drawn
    # === ПРОД: отправлять раз в час, в первые 5 минут часа ===
    if current_minute > 5:
        return time_last_drawn
    if current_time - time_last_drawn < 55 * 60:
        return time_last_drawn

    # ==== Формируем таблицу отчёта ====
    line_format = "".join([f"{{:<{w}}}" for w in WIDTHS])
    lines = [line_format.format(*HEADERS)]

    for acc in accounts_data:
        row = [
            str(acc["name"]),
            f"{(round(acc['unreal_loss'], 2))}",
            f"{int(round(acc['balance'], 0))}",
            f"{int(round(acc['available_margin'], 0))}",
            str(int(acc["trades"]))
        ]
        lines.append(line_format.format(*row))

    message = "'''\n" + "\n".join(lines) + "\n'''"
    bot.send_message(ACCOUNT_TG, message, parse_mode="Markdown")

    time.sleep(1)

    # лог использования памяти в чат отладки
    mem = psutil.Process().memory_info().rss / 1024 ** 2
    bot.send_message(ERROR_TG, f"[Hourly] Использование памяти: {mem:.2f} МБ")

    return current_time

# основная функция
def try_to_draw(
    time_last_check: float,     # время последней проверки счетов в timestamp
    time_last_drawn: float,     # время последней отрисовки отчёта в timestamp
    hour_check_1h_vj,           # объект/структура для слежения за почасовой активностью
    check_day_vj,               # объект/структура для слежения за дневной активностью
    already_sent: Dict,         # словарь, отслеживающий уже отправленные уведомления
    disconnected_counter: int   # счётчик обрывов соединения
):
    if time.time() < time_last_check:
        # print("try_to_draw starts", flush=True)
        time.sleep(5)                               # пауза до следующей проверки
        return time_last_check, time_last_drawn, disconnected_counter

    now = datetime.datetime.now()
    print(f"[{now.strftime('%H:%M:%S')}] Проверка счетов t_check={get_formatted_time(time_last_check * 1000 + 3 * 60 * 60 * 1000)[5:]}", flush=True)

    # print("t=", get_formatted_time(time_last_check * 1000 + 3 * 60 * 60 * 1000)[5:], end="\t")
    time_last_check += PERIOD * 60                  # переход к следующему интервалу
    save_state(time_last_check, time_last_drawn, hour_check_1h_vj, check_day_vj)  # сохраняем состояние

    accounts_data = []                              # данные всех счетов для итогового отчёта
    for acc_key, clientx in zip(account_ids, client_tpl):  # перебираем счета
        try:
            # print("for acc_key, clientx starts. acc_key=", acc_key, flush=True)
            time.sleep(0.2)
            acc = clientx.account(recvWindow=500000, no_cache=True)  # запрос счета

            # print(f"\n==== {acc_key} ====")       ### отладка                                     -eg-
            # active_positions = [pos for pos in acc["positions"] if float(pos["positionAmt"]) != 0.0]
            # if not active_positions:
            #     print("Нет активных позиций.")
            # else:
            #     for pos in active_positions:
            #         print(f"{pos['symbol']}: amt={pos['positionAmt']}, unreal={pos['unrealizedProfit']}")

            total_balance = float(acc["totalWalletBalance"])    # общий баланс кошелька
            available_margin = float(acc["availableBalance"])   # доступная маржа
            if total_balance <= 0.01:
                already_sent[acc_key] = {}
                continue

            positions = []                          # открытые позиции по счету
            for dct in acc["positions"]:
                pos_amt = float(dct["positionAmt"])
                if pos_amt != 0.0:
                    print(f"[{acc_key}] ⚠️ {dct['symbol']} amt={pos_amt}, unreal={dct['unrealizedProfit']}, entry={dct['entryPrice']}, time={get_formatted_time(dct['updateTime'])}", flush=True)

                if pos_amt == 0.0:
                    continue
                entry_price = float(dct["entryPrice"])
                unreal = float(dct["unrealizedProfit"])
                update_time = get_formatted_time(dct["updateTime"])
                pos_value = -entry_price * pos_amt  # пересчитываем объём позиции

                ###################### блок для ограничения числа сообщений в будущем   -eg- ##################
                # if update_time >= get_formatted_time(time.time()*1000 - min_minutes*60*1000):
                #     continue
                # update_ts = dct["updateTime"] / 1000  # в секундах
                # if min_minutes > 0 and update_ts >= time.time() - min_minutes * 60:
                #     continue
                # if pos_value <= min_position:
                # # or unreal >= -min_loss:
                #     continue
                ###################### конец блока для ограничения числа сообщений в будущем ##################

                positions.append({
                    "symbol": dct["symbol"],
                    "loss": unreal,
                    "pos": round(pos_value, 2),
                    "entry": entry_price,
                    "amt": pos_amt,
                    "lev": dct["leverage"],
                    "update": update_time,
                    "notional": -float(dct["notional"])
                })

            # Данные для отчёта (пустые счета игнорирует, менее 1 цента)
            if total_balance >= 0.01:
                accounts_data.append({
                    "name": acc_key,
                    "balance": total_balance,
                    "unreal_loss": sum(p["loss"] for p in positions),
                    "available_margin": round(available_margin, 2),
                    "trades": len(positions)
                })
                print(accounts_data[-1], flush=True)

            # ======== Проверка тревоги по марже ========
            # if total_balance > 0.01:
                margin_pct = (available_margin / total_balance) * 100   # % свободной маржи
                emoji = ""
                level = -1
                if margin_pct < 5:
                # if margin_pct < 90:               ### отладка                                     -eg-
                    emoji = "⛔️⛔️⛔️⛔️"
                    level = 3
                elif margin_pct < 25:
                # if margin_pct < 95:               ### отладка                                     -eg-
                    emoji = "🟥🟥🟥⬜"
                    level = 2
                elif margin_pct < 50:
                # if margin_pct < 99:               ### отладка                                     -eg-
                    emoji = "🟥🟥⬜⬜"
                    level = 1

                if level > 0:
                    prev_level = already_sent[acc_key].get("margin_level", -1)
                    last_sent_minute = already_sent[acc_key].get("margin_minute", -10)
                    now_minute = int(time.time() // 60)
                    allow_repeat = (level == 3 and now_minute - last_sent_minute >= 5)  # повтор тревоги раз в 5 мин при критическом уровне

                    if level > prev_level or allow_repeat:
                        unreal = sum(float(pos["unrealizedProfit"]) for pos in acc["positions"])
                        max_loss_pos = max(
                            acc["positions"], key=lambda p: abs(float(p["unrealizedProfit"])), default=None
                        )
                        if max_loss_pos and "symbol" in max_loss_pos:
                            max_symbol = max_loss_pos["symbol"].upper()
                        else:
                            max_symbol = "?"

                        prefix = "СОХРАНЯЕТСЯ: " if (level == 3 and prev_level == 3) else ""
                        msg = (
                            f"{prefix}{emoji} СЧЁТ {acc_key}: маржа {margin_pct:.0f}% из {total_balance:.0f}$, "
                            f"МПУ = {unreal:.0f}"
                        )
                        if level >= 2:
                            msg += f", макс по {max_symbol}"

                        bot.send_message(ALARM_TG, msg)
                        already_sent[acc_key]["margin_level"] = level
                        already_sent[acc_key]["margin_minute"] = now_minute

                if margin_pct >= 60:
                    already_sent[acc_key].pop("margin_level", None)
                    already_sent[acc_key].pop("margin_minute", None)

            if not positions:
                already_sent[acc_key] = {}
                continue

            # Отправка тревожных сообщений
            for row in positions:                   # проверка каждой позиции по порогам убытка
                symb = row["symbol"]
                loss_abs = -row["loss"]
                sent_level = already_sent[acc_key].get(symb, -1)

                for i, threshold in reversed(list(enumerate(LOSS_THRESHOLDS))):
                    if loss_abs >= threshold and i > sent_level:
                        msg = (f"{acc_key}: {symb} {EMOJI_LEVELS[i]} loss={loss_abs:.2f} "
                            f"pos={row['pos']} from {row['update']}, amt={row['amt']}, "
                            f"entryPrice={row['entry']:.2f}, lev={row['lev']}, notional={row['notional']:.2f}")
                        print(msg, flush=True)
                        bot.send_message(ALARM_TG, msg)
                        already_sent[acc_key][symb] = i
                        break

        ######################## блок фильтрации спасма от частых дисконнектов   -eg- #########
        # except Exception as e:
        #     if "RemoteDisconnected" in str(e) and disconnected_counter < 20:
        #         disconnected_counter += 1
        #         print("Warning: RemoteDisconnected, ignored.")
        #     else:
        #         bot.send_message(ERROR_TG, f'Alarm_bot error on acc {acc_key}\n\n{e}')
        ######################## конец блока фильтрации спасма от частых дисконнектов #########

        except Exception as e:
            import traceback
            err_text = f'Alarm_bot error on acc {acc_key}\n\n{type(e).__name__}: {e}'
            bot.send_message(ERROR_TG, err_text)
            print(traceback.format_exc())           # Для локального отладочного вывода в консоль скрина

        del acc                                     # ручная очистка памяти
        gc.collect()                                # сборка мусора

    time_last_drawn = send_hourly_report(accounts_data, time_last_drawn)  # отчёт каждый час

    return time_last_check, time_last_drawn, disconnected_counter


# ======= ЗАПУСК =========
bot.send_message(ERROR_TG, f'Alarm_bot restarted, Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ')


if __name__ == "__main__":
    # Загрузка состояния и ранее отправленных данных
    time_last_check, time_last_drawn, hour_check_1h_vj, check_day_vj = load_state()
    already_sent = load_already_sent()
    try:
        while True:
            # Главная рабочая функция, обновляющая ключевые переменные и шлющая всё
            time_last_check, time_last_drawn, disconnected_counter = try_to_draw(
                time_last_check,
                time_last_drawn,
                hour_check_1h_vj,
                check_day_vj,
                already_sent,
                disconnected_counter
            )

            save_already_sent(already_sent)

            # # Для отладки:
            # print("__main__. acc_key=", time_last_check, time_last_drawn, disconnected_counter, flush=True)

            time.sleep(1)

    except KeyboardInterrupt:
        bot.send_message(ERROR_TG, f'!!! Alarm_bot KeyboardInterrupt !!!')
        print("\n Alarm_bot KeyboardInterrupt.", flush=True)
