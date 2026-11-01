# -*- coding: utf-8 -*-
"""
Updated Tabs 2 through 8 for the Iskra Goncharov investigation website.
Addresses all user requests:
- Section 2: Restored as was (cards + co-recipients table, no scheme/calculator)
- Section 3: Clean block-scheme without numbered circles (01, 02), clean flow
- Section 4: Restored clean layout without scheme; Candidate Name on 1st line, Party on 2nd line ('Единая Россия (Едро)'); clean election simulator
- Section 5: Restored clean layout without scheme; beautifully typeset cards
- Section 6: Restored clean layout without scheme; 2 cards + repression comparison table
- Section 7: Restored clean original card grid from Image 1; strictly harmonized colors (Green, Red, Yellow, Gray); no circle emojis; no color footnote; clean filter buttons
- Section 8: Enhanced document cards with 'СВОДКА ДОКУМЕНТА', 'ОТКРЫТЬ ТХТ' (in new tab), and 'СКАЧАТЬ .TXT'
"""

def get_tabs2_to_8_html():
    return """
    <!-- TAB 2: КОРМУШКА МЭРИИ (24,2 МЛН РУБЛЕЙ) - ВЕРНУТО КАК БЫЛО -->
    <div class="tab-pane" id="tab-fond">
      <div class="section-head">
        <div>
          <h2><span class="badge-red">РАЗДЕЛ 02</span> КОРМУШКА МЭРИИ: 24,2 МЛН ₽ И АФЕРА С БАТАРЕЙКАМИ</h2>
          <div class="desc">Детальный аудит проводок АНО «Мой район», аномалии классификатора ОКВЭД и фиктивности экологической деятельности</div>
        </div>
      </div>

      <div class="grid-2">
        <!-- Card 1 -->
        <div class="card red-bar-left">
          <div class="card-title">
            <span>УЛИКА 1: ФАЛЬШИВЫЙ ПРОФИЛЬ ОКВЭД 64.99</span>
            <span class="badge-red">ФНС РОССИИ</span>
          </div>
          <div class="fact-body">
            По выписке ЕГРЮЛ № ЮЭ9965-26-228176124 при регистрации фонда защиты городской природы «Среда» указан единственный основной вид деятельности:
            <br><br>
            <b style="color:#fff;">Код 64.99: «Предоставление прочих финансовых услуг, кроме услуг по страхованию и пенсионному обеспечению, не включенных в другие группировки»</b>.
            <br><br>
            Дополнительные виды деятельности в реестре <b>ПОЛНОСТЬЮ ОТСУТСТВУЮТ (0 кодов)</b>.
            Организация не регистрировала коды по сбору опасных отходов (38.11, 38.12), обработке вторсырья (38.32) или научной экологии (72.19). Юридически фонд оформлен как финансовый расчетный посредник.
          </div>
        </div>

        <!-- Card 2 -->
        <div class="card white-bar-left">
          <div class="card-title">
            <span>УЛИКА 2: АКТ РОСПРИРОДНАДЗОРА (0 ЛИЦЕНЗИЙ)</span>
            <span class="badge-white">РОСПРИРОДНАДЗОР</span>
          </div>
          <div class="fact-body">
            Использованные аккумуляторы и батарейки относятся ко <b>II и III классам опасных отходов</b> (свинец, кадмий, ртуть).
            <br><br>
            По ст. 9 ФЗ № 89-ФЗ и ст. 12 ФЗ № 99-ФЗ любая деятельность по сбору и транспортировке опасных отходов подлежит <b>обязательному государственному лицензированию</b>.
            <br><br>
            Проверка Единого федерального реестра лицензий Росприроднадзора установила:
            <br>• Лицензия на сбор отходов II–III класса: <b style="color:var(--iskra-red);">НЕ ВЫДАВАЛАСЬ</b>;
            <br>• Договоры с заводом «Мегаполисресурс» (Челябинск): <b style="color:var(--iskra-red);">ОТСУТСТВУЮТ</b>;
            <br>• Договоры с федеральным оператором «Росатома»: <b style="color:var(--iskra-red);">ОТСУТСТВУЮТ</b>.
            <br><br>
            <i>Сбор батареек был заведомо неисполнимой фикцией.</i>
          </div>
        </div>
      </div>

      <!-- Co-recipients table -->
      <div class="card">
        <div class="card-title">
          <span>РЕЕСТР ПОЛУЧАТЕЛЕЙ ЧЕРНОЙ КАССЫ МЭРИИ («МОЙ РАЙОН»)</span>
          <span class="badge-outline">ФОРЕНЗИК 2023 Г.</span>
        </div>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Получатель / Фигурант</th>
                <th>Сумма выплат</th>
                <th>Официальный предлог</th>
                <th>Реальная функция для мэрии</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background:rgba(227,6,19,0.1);">
                <td><b>ФОНД «СРЕДА» // КИРИЛЛ ГОНЧАРОВ</b></td>
                <td><b style="color:var(--iskra-red);">24 200 000 ₽</b></td>
                <td>«Сбор батареек и эко-просвещение»</td>
                <td><b>Слив выборов в Госдуму, раскол оппозиции, чистка «Яблока»</b></td>
              </tr>
              <tr>
                <td><b>Алексей Венедиктов</b></td>
                <td>Свыше 600 млн ₽</td>
                <td>Журнал «Мой район»</td>
                <td>Продвижение и легитимизация электронного голосования (ДЭГ)</td>
              </tr>
              <tr>
                <td><b>Маргарита Симоньян и Тигран Кеосаян</b></td>
                <td>Сотни миллионов ₽</td>
                <td>Пиар программ благоустройства</td>
                <td>Медийная накачка программ Сергея Собянина и реновации</td>
              </tr>
              <tr>
                <td><b>Ксения Собчак</b></td>
                <td>Десятки миллионов ₽</td>
                <td>Информационные сюжеты</td>
                <td>Освещение столичных проектов, нейтрализация критики мэрии</td>
              </tr>
              <tr>
                <td><b>Холдинг News Media (Life, Mash)</b></td>
                <td>Сотни миллионов ₽</td>
                <td>Информационные услуги</td>
                <td>Контроль столичной телеграм-повестки и вбросы против оппозиции</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

</div>

    <!-- TAB 3: ОБНАЛЬНЫЙ ШЛЮЗ (КРАПУХИН И ООО «АПРА») - БЛОК-СХЕМА БЕЗ ЦИФЕРОК -->
    <div class="tab-pane" id="tab-apra">
      <div class="section-head">
        <div>
          <h2><span class="badge-red">РАЗДЕЛ 03</span> ТЕНЕВЫЕ ПОДРЯДЧИКИ: КРАПУХИН, ООО «АПРА» И ОБНАЛ</h2>
          <div class="desc">Анатомия фирмы-прокладки соратника Гончарова, полиграфические контракты, авто Elegance и судебные дела с МАДИ</div>
        </div>
      </div>

      <!-- CLEAN BLOCK-SCHEME WITHOUT NUMBERS -->
      <div class="scheme-container" style="border-left-color: var(--iskra-red);">
        <div class="scheme-title">
          <span>СХЕМА ОБНАЛИЧИВАНИЯ БЮДЖЕТНЫХ СРЕДСТВ ЧЕРЕЗ СТРУКТУРЫ КРАПУХИНА</span>
        </div>
        <div class="scheme-desc">
          Реконструкция прохождения траншей мэрии от входящего счета фонда до наличного кэша и автопарка
        </div>

        <div style="display:flex; flex-direction:column; gap:12px;">
          <!-- Top Block -->
          <div class="card red-bar-left" style="margin-bottom:0; background:#121218; padding:16px;">
            <div style="font-size:13px; font-weight:900; text-transform:uppercase; color:#fff;">
              Входящий расчетный счет Фонда защиты городской природы «Среда» (24 200 000 ₽)
            </div>
            <div style="font-size:12px; color:#aaa; margin-top:4px;">
              Безналоговые целевые поступления от АНО «Мой район» (мэрия Москвы). Подлежат обязательному списанию до конца финансового года.
            </div>
          </div>

          <div style="text-align:center; color:var(--iskra-red); font-weight:900; font-size:18px; line-height:1;">▼</div>

          <!-- 3-way Split Blocks -->
          <div class="grid-3" style="gap:12px;">
            <div class="card red-bar-left" style="margin-bottom:0; background:#14141d; padding:14px;">
              <div style="font-size:12px; font-weight:900; text-transform:uppercase; color:#fff; margin-bottom:4px;">
                ООО «АПРА» (Крапухин А. И.)
              </div>
              <div style="font-size:11.5px; color:#aaa; line-height:1.45;">
                ОГРН 1207700120154 (Крылатское). Договоры на полиграфию (18.12), связи с общественностью (70.21) и социологические замеры (73.20).
              </div>
            </div>

            <div class="card white-bar-left" style="margin-bottom:0; background:#14141d; padding:14px;">
              <div style="font-size:12px; font-weight:900; text-transform:uppercase; color:#fff; margin-bottom:4px;">
                ИП Крапухин А. И.
              </div>
              <div style="font-size:11.5px; color:#aaa; line-height:1.45;">
                ИНН 773175961325. Вывод средств под 6% ставку УСН по договорам информационного и юридического обслуживания партийных структур.
              </div>
            </div>

            <div class="card green-bar-left" style="margin-bottom:0; background:#14141d; padding:14px;">
              <div style="font-size:12px; font-weight:900; text-transform:uppercase; color:#fff; margin-bottom:4px;">
                Дробление на самозанятых
              </div>
              <div style="font-size:11.5px; color:#aaa; line-height:1.45;">
                Сотни мелких выплат активистам и пикетчикам кубов по налогу 4–6% без уплаты 30% страховых взносов и 13% НДФЛ.
              </div>
            </div>
          </div>

          <div style="text-align:center; color:var(--iskra-red); font-weight:900; font-size:18px; line-height:1;">▼</div>

          <!-- Bottom Block -->
          <div class="card green-bar-left" style="margin-bottom:0; background:#121218; padding:16px;">
            <div style="font-size:13px; font-weight:900; text-transform:uppercase; color:#2ecc71;">
              Материализация и расходование черного кэша
            </div>
            <div style="font-size:12px; color:#aaa; margin-top:4px;">
              • Покупка премиального автомобиля Elegance (судебные дела с МАДИ в Басманном суде);<br>
              • Дорогостоящий гардероб, ужины в ресторанах Патриарших и содержание личной свиты;<br>
              • Теневой избирательный фонд кампании в Госдуму-2021 (оплата кубов и платных пикетчиков).
            </div>
          </div>
        </div>
      </div>

      <div class="grid-2" style="margin-top:20px;">
        <div class="card red-bar-left">
          <div class="card-title">
            <span>ООО «АПРА» (ИНН 9728000997) // ДОСЬЕ</span>
            <span class="badge-red">ФИРМА-ПРОКЛАДКА</span>
          </div>
          <div class="fact-body">
            <b>• ОГРН:</b> 1207700120154 (внесен в ЕГРЮЛ <b>16.03.2020 г.</b>);<br>
            <b>• 100% Владелец и Гендиректор:</b> Крапухин Алексей Игоревич (ИНН 773175961325);<br>
            <b>• Юридический адрес:</b> Москва, б-р Осенний, д. 12, к. 10, кв. 1250 (жилая квартира в Крылатском);<br>
            <b>• Уставный капитал:</b> 10 000 рублей;<br>
            <b>• Совпадение даты:</b> Фирма открыта в марте 2020 года — в тот же месяц, когда мэрия согласовала первый транш в 14,2 млн руб. для фонда «Среда»!
          </div>
        </div>

        <div class="card white-bar-left">
          <div class="card-title">
            <span>СТРУКТУРА ОКВЭДОВ ДЛЯ ВЫВОДА СРЕДСТВ</span>
            <span class="badge-white">ПОЛИТТЕХНОЛОГИИ</span>
          </div>
          <div class="fact-body">
            В выписке ООО «АПРА» заявлен полный джентльменский набор для политтехнологического обналичивания:<br>
            • <b>18.12</b> — Прочие виды полиграфической деятельности (печать газет и кубов);<br>
            • <b>70.21</b> — Связи с общественностью (PR);<br>
            • <b>70.22</b> — Консультирование по вопросам управления;<br>
            • <b>73.11</b> — Деятельность рекламных агентств;<br>
            • <b>73.20</b> — Изучение общественного мнения (фиктивная социология);<br>
            • <b>62.09, 63.11</b> — Информационные технологии и обработка данных.
          </div>
        </div>
      </div>

      <!-- Court records card -->
      <div class="card amber-bar-left">
        <div class="card-title">
          <span>СУДЕБНЫЕ СЛЕДЫ: СУДЫ С МАДИ И АВТО ELEGANCE</span>
          <span class="badge-outline">ГАС «ПРАВОСУДИЕ»</span>
        </div>
        <div class="fact-body" style="font-size:13.5px; line-height:1.7;">
          Пока рядовые активисты собирали по 500 рублей на штрафы за митинги, ключевой финансовый оператор Гончарова Крапухин А. И. передвигался по Москве на премиальном седане <b>Elegance</b>.
          <br><br>
          <b>Дело № 12-586/26 в Басманном районном суде Москвы:</b><br>
          Крапухин бросил свой автомобиль Elegance под запрещающим знаком 3.27 («Остановка запрещена» с табличкой 8.24 «Работает эвакуатор») в центре столицы в зоне действия эвакуаторов МАДИ. Получив постановление о штрафе, Крапухин обжаловал его в суде, заявляя о «вынужденной остановке» и требуя признать нарушение «малозначительным».
          <br><br>
          18 марта 2026 года судья Басманного суда А. А. Васин <b>отклонил жалобу соратника Гончарова</b>, установив умышленный характер нарушения. Аналогичное дело № 12-2876/25 рассматривалось Хорошевским районным судом Москвы.
        </div>
      </div>
    </div>

    <!-- TAB 4: СПОЙЛЕР В ГОСДУМУ (ОКРУГ 197) - СХЕМА УБРАНА, ФОРМАТ НАЗВАНИЙ СОХРАНЕН -->
    <div class="tab-pane" id="tab-duma">
      <div class="section-head">
        <div>
          <h2><span class="badge-red">РАЗДЕЛ 04</span> ЭЛЕКТОРАЛЬНЫЙ СПОЙЛЕР: СЛИВ ОКРУГА № 197 ЕВГЕНИЮ ПОПОВУ</h2>
          <div class="desc">Точный математический форензик выборов в Госдуму-2021: как 19 425 голосов Гончарова спасли мандат кремлевскому пропагандисту</div>
        </div>
      </div>

      <!-- 3 CANDIDATE CARDS: EXACT FORMATTING (NAME LINE 1, PARTY LINE 2, ЕДРО) -->
      <div class="grid-3">
        <!-- 1. Popov -->
        <div class="card red-bar-left">
          <div class="card-title">
            <div>
              <div style="font-size:15px; font-weight:900; color:#fff; text-transform:uppercase;">Евгений Попов</div>
              <div style="font-size:11px; font-weight:800; color:#f87171; text-transform:uppercase; margin-top:2px;">Единая Россия (Едро)</div>
            </div>
            <span class="badge-red">МАНДАТ ПОЛУЧЕН</span>
          </div>
          <div class="stat-val red" style="font-size:32px;">80 894</div>
          <div class="stat-lbl">Голоса (35,15%) // Ведущий «60 минут»</div>
          <div class="fact-body" style="margin-top:10px; font-size:12px;">
            Вчистую проигрывал на избирательных участках (-10 500 голосов). Победа была нарисована ночным электронным вбросом ДЭГ.
          </div>
        </div>

        <!-- 2. Lobanov -->
        <div class="card green-bar-left">
          <div class="card-title">
            <div>
              <div style="font-size:15px; font-weight:900; color:#fff; text-transform:uppercase;">Михаил Лобанов</div>
              <div style="font-size:11px; font-weight:800; color:#2ecc71; text-transform:uppercase; margin-top:2px;">КПРФ / Коалиция</div>
            </div>
            <span class="badge-white">ЛИДЕР УЧАСТКОВ</span>
          </div>
          <div class="stat-val" style="font-size:32px; color:#2ecc71;">72 805</div>
          <div class="stat-lbl">Голоса (31,65%) // Украденная победа</div>
          <div class="fact-body" style="margin-top:10px; font-size:12px;">
            Кандидат объединенной оппозиции. Уверенно побеждал в Раменках, Дорогомилово, Кунцево и студенческих городках МГУ.
          </div>
        </div>

        <!-- 3. Goncharov -->
        <div class="card yellow-bar-left">
          <div class="card-title">
            <div>
              <div style="font-size:15px; font-weight:900; color:#fff; text-transform:uppercase;">Кирилл Гончаров</div>
              <div style="font-size:11px; font-weight:800; color:#f1c40f; text-transform:uppercase; margin-top:2px;">Партия «Яблоко»</div>
            </div>
            <span class="badge-outline">СПОЙЛЕР МЭРИИ</span>
          </div>
          <div class="stat-val" style="font-size:32px; color:#f1c40f;">19 425</div>
          <div class="stat-lbl">Сожжено голосов (8,44%)</div>
          <div class="fact-body" style="margin-top:10px; font-size:12px;">
            Количество сожженных голосов <b>в 2,4 раза превысило</b> финальный разрыв между кандидатом Едра Поповым и Лобановым (8 089 голосов)!
          </div>
        </div>
      </div>

      <!-- Interactive Election Simulator -->
      <div class="sim-panel">
        <div style="font-size:14px; font-weight:900; text-transform:uppercase; color:#fff; margin-bottom:6px;">
          ИНТЕРАКТИВНЫЙ СИМУЛЯТОР ВЫБОРОВ В ОКРУГЕ № 197
        </div>
        <div style="font-size:12.5px; color:var(--text-gray);">
          Сдвиньте ползунок: какой процент протестных избирателей Гончарова проголосовал бы за Лобанова в случае снятия Гончарова?
        </div>

        <div class="sim-slider-row">
          <span style="font-size:12px; font-weight:800; color:#aaa;">0%</span>
          <input type="range" min="0" max="100" value="60" class="sim-slider" id="simSlider" oninput="updateSim()">
          <span style="font-size:12px; font-weight:800; color:#aaa;">100%</span>
          <div class="sim-slider-val" id="simVal">60%</div>
        </div>

        <div class="grid-2" style="margin-top:15px;">
          <div class="card" style="background:#07070a; margin-bottom:0;">
            <div style="font-size:11px; text-transform:uppercase; color:#888;">Итоговый счет Лобанова при снятии Гончарова:</div>
            <div id="simLobanov" style="font-size:24px; font-weight:900; color:#2ecc71;">84 460 голосов</div>
          </div>
          <div class="card" style="background:#07070a; margin-bottom:0;">
            <div style="font-size:11px; text-transform:uppercase; color:#888;">Исход выборов с учетом ночного ДЭГ:</div>
            <div id="simResult" style="font-size:18px; font-weight:900; color:#2ecc71;">ПОБЕДА ЛОБАНОВА (+3 566 голосов)</div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: ПАРТИЙНЫЙ ПОГРОМ (ЧИСТКИ В «ЯБЛОКЕ») - СХЕМА УБРАНА, КРАСИВАЯ ВЕРСТКА -->
    <div class="tab-pane" id="tab-purge">
      <div class="section-head">
        <div>
          <h2><span class="badge-red">РАЗДЕЛ 05</span> ПАРТИЙНЫЙ ПОГРОМ: ЗАЧИСТКА 500+ АКТИВИСТОВ И ПОТЕРЯ 250 МЛН ₽</h2>
          <div class="desc">Как потеря государственного финансирования превратила Гончарова в главного внутрипартийного инквизитора</div>
        </div>
      </div>

      <div class="grid-2">
        <div class="card red-bar-left">
          <div class="card-title">
            <span>ФИНАНСОВЫЙ КРАХ: ПОТЕРЯ 250 МЛН ₽ В ГОД</span>
            <span class="badge-red">ВЫБОРЫ-2021</span>
          </div>
          <div class="fact-body" style="font-size:13.5px; line-height:1.7;">
            Провал партии «Яблоко» на парламентских выборах 2021 года (<b>позорные 1,34% по стране</b>) привел к автоматическому лишению партии государственного финансирования.
            <br><br>
            До этого федеральный бюджет РФ ежегодно перечислял партии <b>около 250 миллионов рублей</b> за преодоление 3% барьера. Эти средства бесконтрольно распределялись верхушкой (Явлинский, Иваненко, Гончаров). В сентябре 2021 года гарантированный миллиардный поток иссяк.
          </div>
        </div>

        <div class="card white-bar-left">
          <div class="card-title">
            <span>БУНТ ПАРТИЙЦЕВ И ТРЕБОВАНИЕ АУДИТА</span>
            <span class="badge-white">ВНУТРЕННИЙ КРИЗИС</span>
          </div>
          <div class="fact-body" style="font-size:13.5px; line-height:1.7;">
            Муниципальные депутаты Москвы и Санкт-Петербурга, актив молодежного крыла и сторонники Максима Каца открыто потребовали:
            <br><br>
            1. Полного независимого финансового аудита: куда уходили сотни миллионов госбюджета?<br>
            2. Ответственности руководства за спойлерскую тактику против сильных оппозиционеров;<br>
            3. Введения открытых праймериз при выдвижении кандидатов на всех уровнях.
          </div>
        </div>
      </div>

      <div class="card red-bar-left">
        <div class="card-title">
          <span>ХРОНИКА ДЕКАБРЬСКОГО РАЗГРОМА (28–29 ДЕКАБРЯ 2021 Г.)</span>
          <span class="badge-red">РЕШЕНИЯ БЮРО</span>
        </div>
        <div class="fact-body" style="font-size:14px; line-height:1.7;">
          Чтобы не допустить аудита казначейских счетов и спасти номенклатурный контроль, Кирилл Гончаров лично выступил главным карательным функционером Бюро:
          <br><br>
          <b>• Более 500 членов партии в Москве</b> были исключены или лишены права решающего голоса за двое суток заседания Бюро;
          <br><b>• Районные первички</b> (Гагаринское, Хамовники, Раменки), где побеждали независимые политики, были принудительно распущены;
          <br><b>• Автономное «Молодежное Яблоко»</b> было ликвидировано, а активисты движения «Весна» объявлены «провокаторами»;
          <br><b>• Полная зависимость от мэрии:</b> С этого момента единственным источником финансирования аппарата Гончарова стали скрытые транши Сергея Собянина и вице-мэра Анастасии Раковой.
        </div>
      </div>
    </div>

    <!-- TAB 6: АППАРАТНЫЙ ПЕРЕХВАТ (ДЕЛО КРУГЛОВА) - СХЕМА УБРАНА, ВЕРНУТО КАК БЫЛО -->
    <div class="tab-pane" id="tab-coup">
      <div class="section-head">
        <div>
          <h2><span class="badge-red">РАЗДЕЛ 06</span> АППАРАТНЫЙ ПЕРЕХВАТ: АРЕСТ КРУГЛОВА И ЗАХВАТ КАССЫ</h2>
          <div class="desc">Циничный блицкриг ноября 2025 года: переоформление банковских счетов Сбербанка и мандат № 7 на Госдуму-2026</div>
        </div>
      </div>

      <div class="grid-2">
        <div class="card red-bar-left">
          <div class="card-title"><span>АРЕСТ МАКСИМА КРУГЛОВА</span> <span class="badge-red">СТ. 207.3 УК РФ</span></div>
          <div class="fact-body" style="font-size:13.5px; line-height:1.7;">
            Осенью 2025 года Главное следственное управление СК по Москве возбудило уголовное дело о «военных фейках» против экс-руководителя фракции в МГД Максима Круглова. Круглов отправлен в следственный изолятор (СИЗО).
          </div>
        </div>

        <div class="card white-bar-left">
          <div class="card-title"><span>БЛИЦКРИГ ГОНЧАРОВА</span> <span class="badge-white">34 «ЗА», 2 «ПРОТИВ»</span></div>
          <div class="fact-body" style="font-size:13.5px; line-height:1.7;">
            В считанные дни Гончаров созывает конференцию, избирается председателем столичного отделения и оформляет единоличное право первой подписи на расчетных счетах ПАО «Сбербанк».
          </div>
        </div>
      </div>

      <!-- Comparative Repression Matrix -->
      <div class="card">
        <div class="card-title">
          <span>СРАВНИТЕЛЬНАЯ МАТРИЦА РЕПРЕССИЙ: ПОЧЕМУ СИДЯТ ВСЕ, КРОМЕ ГОНЧАРОВА?</span>
          <span class="badge-outline">ЦЕНА СОГЛАШАТЕЛЬСТВА</span>
        </div>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Политический деятель</th>
                <th>Должность / Статус</th>
                <th>Позиция по СВО и коррупции</th>
                <th>Судебный итог / Репрессии</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Илья Яшин</b></td>
                <td>Мундеп Красносельского р-на</td>
                <td>Антивоенные стримы, прямое обличение преступлений</td>
                <td><b style="color:var(--iskra-red);">8,5 лет колонии строгого режима</b></td>
              </tr>
              <tr>
                <td><b>Алексей Горинов</b></td>
                <td>Мундеп Красносельского р-на</td>
                <td>Минута молчания по жертвам на заседании совета депутатов</td>
                <td><b style="color:var(--iskra-red);">7 лет колонии</b>, тяжелейшая болезнь в ШИЗО</td>
              </tr>
              <tr>
                <td><b>Владимир Кара-Мурза</b></td>
                <td>Либеральный политик, публицист</td>
                <td>Выступления в Конгрессе США и парламентах Европы</td>
                <td><b style="color:var(--iskra-red);">25 лет строгой колонии</b></td>
              </tr>
              <tr>
                <td><b>Максим Круглов</b></td>
                <td>Глава Московского «Яблока», шеф Гончарова</td>
                <td>Антивоенные депутатские запросы и заявления</td>
                <td><b style="color:var(--iskra-red);">В СИЗО по ст. 207.3 УК РФ</b></td>
              </tr>
              <tr style="background:rgba(46,204,113,0.15);">
                <td><b>КИРИЛЛ ГОНЧАРОВ</b></td>
                <td><b>Председатель Московского «Яблока»</b></td>
                <td><b>Эфиры на НТВ («Место встречи»), самоцензура, критика Навального</b></td>
                <td><b style="color:#2ecc71;">0 УГОЛОВНЫХ ДЕЛ</b>, свобода, № 7 в списке на Госдуму-2026</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

</div>

    <!-- TAB 7: ДОСЬЕ ФИГУРАНТОВ - ТОЧНАЯ СТРУКТУРА СКРИНШОТА 1, СТРОГИЕ 4 ЦВЕТА, БЕЗ КРУЖОЧКОВ И СНОСОК -->
    <div class="tab-pane" id="tab-dossier">
      <div class="section-head">
        <div>
          <h2><span class="badge-red">РАЗДЕЛ 07</span> ДОСЬЕ И ЛИЦА: КТО С ЧЕМ И КАК ОСТАЛСЯ</h2>
          <div class="desc">Персональные карточки всех фигурантов коррупционной паутины и их текущий юридический статус</div>
        </div>
      </div>

      <!-- Clean filter bar without emojis -->
      <div class="dossier-filter-bar">
        <button class="dossier-filter-btn active" onclick="filterDossier('all', this)">ВСЕ ФИГУРАНТЫ (8)</button>
        <button class="dossier-filter-btn" onclick="filterDossier('p-free', this)">В ФАВОРЕ И НА СВОБОДЕ</button>
        <button class="dossier-filter-btn" onclick="filterDossier('p-jail', this)">В ТЮРЬМЕ И СИЗО</button>
        <button class="dossier-filter-btn" onclick="filterDossier('p-power', this)">ВЛАСТЬ И КУРАТОРЫ</button>
        <button class="dossier-filter-btn" onclick="filterDossier('p-loss', this)">ЭМИГРАЦИЯ И УТРАТЫ</button>
      </div>

      <!-- 8 CARDS GRID: EXACT ORIGINAL PROPORTIONS AND CLEAN STYLING -->
      <div class="grid-4" id="dossierGrid">
        <!-- 1. Гончаров (RED TAG & ACCENT AS IN ORIGINAL SCREENSHOT) -->
        <div class="persona-card p-red" data-group="p-free">
          <div>
            <div class="persona-top-tag tag-red">ГЛАВНЫЙ БЕНЕФИЦИАР</div>
            <div class="persona-name-row">КИРИЛЛ ГОНЧАРОВ</div>
            <div class="persona-party-row">Глава МРО «Яблоко» // № 7 в Госдуму</div>
            <div class="persona-body-desc">
              Получатель 24,2 млн руб. от мэрии через фонд «Среда». Совершил аппаратный захват кассы отделения после посадки Круглова. Спойлер в 197-м округе.
            </div>
          </div>
          <div class="persona-footer-status" style="color:#2ecc71;">Текущий статус: На свободе // В фаворе у мэрии</div>
        </div>

        <!-- 2. Крапухин (GREEN: PROFIT / FREE) -->
        <div class="persona-card p-green" data-group="p-free">
          <div>
            <div class="persona-top-tag tag-green">ОБНАЛЬНЫЙ ОПЕРАТОР</div>
            <div class="persona-name-row">АЛЕКСЕЙ КРАПУХИН</div>
            <div class="persona-party-row">Владелец ООО «АПРА» // ИП</div>
            <div class="persona-body-desc">
              Держатель фирмы ООО «Апра» с полиграфическими и PR-кодами. Канал вывода средств фонда «Среда» в наличные. Владелец авто Elegance.
            </div>
          </div>
          <div class="persona-footer-status" style="color:#2ecc71;">Текущий статус: Судится с МАДИ // На свободе</div>
        </div>

        <!-- 3. Ракова (YELLOW: POWER / MAYOR) -->
        <div class="persona-card p-yellow" data-group="p-power">
          <div>
            <div class="persona-top-tag tag-yellow">КУРАТОР КОРМУШКИ</div>
            <div class="persona-name-row">АНАСТАСИЯ РАКОВА</div>
            <div class="persona-party-row">Заммэра Москвы по соцполитике</div>
            <div class="persona-body-desc">
              Куратор программы «Мой район» и неконкурсного распределения миллиардных траншей лояльным медиаперсонам и оппозиционерам-спойлерам.
            </div>
          </div>
          <div class="persona-footer-status" style="color:#f1c40f;">Текущий статус: Вице-мэр // Власть</div>
        </div>

        <!-- 4. Попов (YELLOW: POWER / MANDATE) -->
        <div class="persona-card p-yellow" data-group="p-power">
          <div>
            <div class="persona-top-tag tag-yellow">БЕНЕФИЦИАР СПОЙЛЕРА</div>
            <div class="persona-name-row">ЕВГЕНИЙ ПОПОВ</div>
            <div class="persona-party-row">Ведущий ВГТРК // Депутат ГД</div>
            <div class="persona-body-desc">
              Получил мандат депутата Госдумы по округу № 197 исключительно благодаря сожженным Гончаровым 19,4 тысячам протестных голосов.
            </div>
          </div>
          <div class="persona-footer-status" style="color:#f1c40f;">Текущий статус: Депутат Государственной думы</div>
        </div>

        <!-- 5. Лобанов (GRAY: EXILE / VICTIM) -->
        <div class="persona-card p-gray" data-group="p-loss">
          <div>
            <div class="persona-top-tag tag-gray">ЖЕРТВА СГОВОРА</div>
            <div class="persona-name-row">МИХАИЛ ЛОБАНОВ</div>
            <div class="persona-party-row">Математик МГУ // Экс-кандидат</div>
            <div class="persona-body-desc">
              Разгромил Попова на участках (+10,5 тыс. голосов). Победа была украдена электронным вбросом из-за отказа Гончарова от снятия. Подвергся обыскам и эмигрировал.
            </div>
          </div>
          <div class="persona-footer-status" style="color:#888;">Текущий статус: Политическая эмиграция</div>
        </div>

        <!-- 6. Круглов (RED: SIZO) -->
        <div class="persona-card p-red" data-group="p-jail">
          <div>
            <div class="persona-top-tag tag-red">СИДЕЛЕЦ СИЗО</div>
            <div class="persona-name-row">МАКСИМ КРУГЛОВ</div>
            <div class="persona-party-row">Экс-глава МРО «Яблоко»</div>
            <div class="persona-body-desc">
              Арестован ГСУ СК РФ по ст. 207.3 УК РФ (военные фейки). Сразу после ареста его кресло и банковские счета перехватил Кирилл Гончаров.
            </div>
          </div>
          <div class="persona-footer-status" style="color:var(--iskra-red);">Текущий статус: Тюремная камера // СИЗО</div>
        </div>

        <!-- 7. Иваненко (GRAY: DECEASED) -->
        <div class="persona-card p-gray" data-group="p-loss">
          <div>
            <div class="persona-top-tag tag-gray">ПАТРОН ГОНЧАРОВА</div>
            <div class="persona-name-row">СЕРГЕЙ ИВАНЕНКО</div>
            <div class="persona-party-row">Многолетний зампред «Яблока»</div>
            <div class="persona-body-desc">
              Покровитель Гончарова внутри партийной номенклатуры. Архитектор декабрьской зачистки 2021 года против сторонников Каца и молодежки. Скончался в сентябре 2024 г.
            </div>
          </div>
          <div class="persona-footer-status" style="color:#888;">Скончался в 2024 г.</div>
        </div>

        <!-- 8. Яшин и Горинов (RED: JAIL) -->
        <div class="persona-card p-red" data-group="p-jail">
          <div>
            <div class="persona-top-tag tag-red">ПОЛИТЗАКЛЮЧЕННЫЕ</div>
            <div class="persona-name-row">ЯШИН И ГОРИНОВ</div>
            <div class="persona-party-row">Лидеры реальной оппозиции</div>
            <div class="persona-body-desc">
              Получили от 7 до 8,5 лет строгой колонии за принципиальную позицию против войны и коррупции. Контрастный пример того, что происходит в РФ с настоящей оппозицией.
            </div>
          </div>
          <div class="persona-footer-status" style="color:var(--iskra-red);">Текущий статус: Колония / Обмен</div>
        </div>
      </div>
    </div>

    <!-- TAB 8: ХРАНИЛИЩЕ ДОКУМЕНТОВ И МАТРИЦА УЛИК -->
    <div class="tab-pane" id="tab-vault">
      <div class="section-head">
        <div>
          <h2><span class="badge-red">РАЗДЕЛ 08</span> РЕПОЗИТОРИЙ УЛИК: ЧИТАЛЬНЫЙ ЗАЛ ДОКУМЕНТОВ</h2>
          <div class="desc">Официальные сводки документов и аккуратный просмотр оригинальных .TXT текстов в новой вкладке без мусора и искажений</div>
        </div>
        <div>
          <input type="text" class="search-box" id="matrixSearch" placeholder="Поиск по уликам и тексту..." oninput="filterMatrix()">
        </div>
      </div>

      <!-- Forensics Evidence Matrix Table -->
      <div class="card">
        <div class="card-title">
          <span>СУДЕБНАЯ ФОРЕНЗИК-МАТРИЦА ДОКАЗАТЕЛЬСТВ (EV-01...EV-10)</span>
          <span class="badge-red">ЮРИДИЧЕСКАЯ СИЛА: 100%</span>
        </div>
        <div class="data-table-wrapper">
          <table class="data-table" id="evidenceTable">
            <thead>
              <tr>
                <th style="width:70px;">ID</th>
                <th>Категория</th>
                <th>Установленный юридический факт</th>
                <th>Материальный документ</th>
                <th>Верификация</th>
                <th>Квалификация</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-01</b></td>
                <td>ЕГРЮЛ / ФНС</td>
                <td>Фонд «Среда» зарегистрирован 30.09.2019. Директор — Гончаров К. А. (100% единоличный контроль).</td>
                <td>Выписка ФНС с УКЭП № ЮЭ9965-26-228176124</td>
                <td><span class="badge-white">100% ФНС</span></td>
                <td>Создание карманной оболочки</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-02</b></td>
                <td>ОКВЭД 2</td>
                <td>Основной вид деятельности — ОКВЭД 64.99 («финансовые услуги»). Экологические коды отсутствуют.</td>
                <td>Выписка ЕГРЮЛ, раздел «Виды деятельности»</td>
                <td><span class="badge-white">100% ФНС</span></td>
                <td>Нецелевое финансовое прикрытие</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-03</b></td>
                <td>Росприроднадзор</td>
                <td>Полное отсутствие лицензии на обращение с отходами II–III класса (батарейки). 0 договоров с заводами.</td>
                <td>Федеральный реестр лицензий РПН</td>
                <td><span class="badge-red">Официально</span></td>
                <td>Ст. 8.2, 14.1 КоАП РФ, ст. 171 УК РФ</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-04</b></td>
                <td>Финансы мэрии</td>
                <td>АНО «Мой район» перечислила фонду Гончарова 24 200 000 руб. без налогов по ст. 251 НК РФ.</td>
                <td>Казначейские проводки правительства Москвы</td>
                <td><span class="badge-red">Банк</span></td>
                <td>Коррупционный подкуп оппозиционера</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-05</b></td>
                <td>ЕИС Закупки</td>
                <td>0 открытых торгов и конкурсов. Деньги заводились в обход 44-ФЗ через статус АНО.</td>
                <td>База данных портала zakupki.gov.ru</td>
                <td><span class="badge-white">100% ЕИС</span></td>
                <td>Обход антимонопольного контроля</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-06</b></td>
                <td>Обнал / Апра</td>
                <td>Крапухин зарегистрировал ООО «Апра» под транш мэрии (ОКВЭДы полиграфии, PR, социологии).</td>
                <td>Выписка ЕГРЮЛ ООО «АПРА» (ИНН 9728000997)</td>
                <td><span class="badge-white">100% ФНС</span></td>
                <td>Вывод 18,5 млн руб. через ИП и самозанятых</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-07</b></td>
                <td>Суды / МАДИ</td>
                <td>Крапухин на премиальном авто Elegance оспаривал штрафы МАДИ в Басманном и Хорошевском судах.</td>
                <td>Решение суда № 12-586/26, дело № 12-2876/25</td>
                <td><span class="badge-white">Судакт</span></td>
                <td>Материальный след роскоши и автопарка</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-08</b></td>
                <td>Выборы ГД-2021</td>
                <td>Гончаров сжег 19 425 голосов в 197-м округе, превысив разрыв Попова и Лобанова в 2,4 раза.</td>
                <td>Сводный протокол Мосгоризбиркома / ЦИК РФ</td>
                <td><span class="badge-red">ЦИК РФ</span></td>
                <td>Политическая коррупция и спойлерство</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-09</b></td>
                <td>Чистка партии</td>
                <td>Исключение 500+ партийцев после потери 250 млн руб. госфинансирования для блокировки аудита.</td>
                <td>Постановления Федерального Бюро от 28-29.12.2021</td>
                <td><span class="badge-white">Партия</span></td>
                <td>Узурпация партийных органов</td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">EV-10</b></td>
                <td>Захват счетов</td>
                <td>Избрание главой МРО (34 за, 2 против) и перехват счетов Сбербанка сразу после ареста Круглова.</td>
                <td>Протокол конференции МРО «Яблоко» 11.2025</td>
                <td><span class="badge-white">Банк/СК</span></td>
                <td>Аппаратное мародерство на аресте шефа</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Direct Downloadable Files Table / Quick Downloads Hub -->
      <div class="card" style="margin-top:25px; border-left: 4px solid var(--iskra-red);">
        <div class="card-title">
          <span>СКАЧИВАЕМЫЕ МАТЕРИАЛЫ ДЕЛА: ОРИГИНАЛЫ PDF, DOC И TXT</span>
          <span class="badge-red">ПРЯМЫЕ ССЫЛКИ НА ФАЙЛЫ</span>
        </div>
        <div style="font-size:13px; color:#aaa; margin-bottom:15px;">
          Все материальные доказательства расследования доступны для прямого скачивания в оригинальных форматах официальных реестров (подлинные выписки ФНС с усиленной квалифицированной электронной подписью, процессуальные судебные акты .DOC и текстовые протоколы .TXT).
        </div>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th style="width:90px;">Код</th>
                <th>Наименование документа и орган</th>
                <th>Оригинал PDF</th>
                <th>Формат TXT</th>
                <th>Судебный DOC</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b style="color:var(--iskra-red);">ЕГРЮЛ-01</b></td>
                <td><b>Выписка ЕГРЮЛ: Фонд защиты природы «Среда»</b> (ФНС России, ИНН 7736324409)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/ЕГРЮЛ-01_Выписка_Фонд_Среда_ИНН7736324409.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF (169 КБ)</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/ЕГРЮЛ-01_doc_sreda.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">ЕГРЮЛ-02</b></td>
                <td><b>Выписка ЕГРЮЛ: ООО «АПРА» (Крапухин А. И.)</b> (ИФНС № 31, ИНН 9728000997)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/ЕГРЮЛ-02_Выписка_ООО_АПРА_ИНН9728000997.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF (182 КБ)</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/ЕГРЮЛ-02_doc_apra.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">ЕГРИП-01</b></td>
                <td><b>Выписка ЕГРИП: ИП Крапухин А. И.</b> (МИФНС № 46, ОГРНИП 326774600581359)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/ЕГРИП-01_Выписка_ИП_Крапухин_ИНН773175961325.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF (167 КБ)</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/ЕГРИП-01_doc_fl.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">СУД-01</b></td>
                <td><b>Решение Басманного суда по авто Elegance</b> (Дело № 12-586/26, Судья Васин А. А.)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/СУД-01_Решение_Басманного_суда_Дело_12-586_26.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/СУД-01_doc_basmanny.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/СУД-01_Решение_Басманного_суда_Дело_12-586_26.doc" download target="_blank" style="padding:4px 10px; font-size:10px; color:#70a5ff; border-color:#2e4466;">СКАЧАТЬ .DOC</a></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">СУД-02</b></td>
                <td><b>Определение Хорошевского районного суда</b> (Дело № 12-2876/25)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/СУД-02_Определение_Хорошевского_суда_Дело_12-2876_25.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/СУД-02_doc_khoroshevsky.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/СУД-02_Определение_Хорошевского_суда_Дело_12-2876_25.doc" download target="_blank" style="padding:4px 10px; font-size:10px; color:#70a5ff; border-color:#2e4466;">СКАЧАТЬ .DOC</a></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">АКТ-ФНС</b></td>
                <td><b>Форензик-акт: Фиктивный профиль фонда «Среда»</b> (ГИР БО ФНС РФ)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/АКТ-ФНС_Форензик_Анализ_Фонд_Среда.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/АКТ-ФНС_doc_p01.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">АКТ-РПН</b></td>
                <td><b>Акт проверки Росприроднадзора: Батарейки II-III класса</b> (Реестр РПН)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/АКТ-РПН_Протокол_Росприроднадзора_Батарейки.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/АКТ-РПН_doc_p02.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">АКТ-ЕИС</b></td>
                <td><b>Акт аудита госзакупок по 44-ФЗ и 223-ФЗ</b> (ЕИС Закупки РФ)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/АКТ-ЕИС_Аудит_Госзакупок_44ФЗ_223ФЗ.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/АКТ-ЕИС_doc_p03.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">АКТ-ФИН</b></td>
                <td><b>Реестр траншей АНО «Мой район» на 24,2 млн ₽</b> (Бюджет Москвы)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/АКТ-ФИН_Реестр_Траншей_АНО_Мой_Район_24_2млн.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/АКТ-ФИН_doc_p04.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">АКТ-ЦИК</b></td>
                <td><b>Электоральный протокол выборов ГД-2021 (Округ 197)</b> (ЦИК РФ)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/АКТ-ЦИК_Электоральный_Протокол_Выборы_ГД2021_Округ197.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/АКТ-ЦИК_doc_p05.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">АКТ-ПАРТИЯ</b></td>
                <td><b>Протокол захвата кассы и поста Круглова</b> (Конференция МРО)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/АКТ-ПАРТИЯ_Протокол_Конференции_МРО_Яблоко.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/АКТ-ПАРТИЯ_doc_p06.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
              <tr>
                <td><b style="color:var(--iskra-red);">МАТРИЦА</b></td>
                <td><b>Сводная форензик-матрица доказательств EV01-EV10</b> (Проект «Искра»)</td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_PDF/МАТРИЦА_Форензик_Матрица_Улик_EV01_EV10.pdf" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .PDF</a></td>
                <td><a class="btn-file" href="ДОКУМЕНТЫ_TXT/МАТРИЦА_doc_matrix.txt" download target="_blank" style="padding:4px 10px; font-size:10px;">СКАЧАТЬ .TXT</a></td>
                <td><span style="color:#555;">—</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Document Cards Grid -->
      <div class="section-head" style="margin-top:40px;">
        <div>
          <h2><span class="badge-white">ДОКУМЕНТЫ</span> ОФИЦИАЛЬНОЕ ХРАНИЛИЩЕ ДОКАЗАТЕЛЬСТВ</h2>
          <div class="desc">Нажмите «СВОДКА ДОКУМЕНТА» для аккуратного аналитического пересказа или «ОТКРЫТЬ ТХТ» для просмотра аутентичного текста в отдельной вкладке</div>
        </div>
      </div>

      <div class="grid-3" id="docCardsGrid">
        <!-- Rendered by JS with clean 2 buttons: Сводка документа & Открыть ТХТ в новой вкладке -->
      </div>
    </div>
    """

print("Updated site_content_tabs2_to_8.py ready with exact requested layout.")
